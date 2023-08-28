from network_monitoring import handle_info_about_host
from db.work_with_table_hosts import WorkWithHosts
from db.work_with_table_inf_host import WorkWithHostStatus
from db.work_with_table_lp import WorkWithLostPackets
from ping_object import PingObject
from queue import Queue
from threading import Thread
from loger import app_loger
from program_voice.python_voice import PyVoice
from playsound import playsound
from temp import run_ping
from time import sleep
from parsing_answer import allocation_to_lists_async
from list_of_hosts_we_work_with import read_current_hosts


class Manager:
    """Класс управления программой"""
    def __init__(self):
        self.wwh = WorkWithHosts()
        self.wwhs = WorkWithHostStatus()
        self.wwlp = WorkWithLostPackets()
        self.list_of_hosts = dict()
        self.fill_list_of_hosts = dict()
        self.mode_work = 'Threads'

    def read_all_hosts(self) -> dict:
        self.fill_list_of_hosts = dict()
        data_from_db = self.wwh.read_all_data()
        for data_about_host in data_from_db:
            ping_obj = PingObject(
                host_id=data_about_host.host_id,
                ip_add=data_about_host.ip_add,
                name=data_about_host.name,
                music=data_about_host.music,
                description=data_about_host.descr,
            )
            self.fill_list_of_hosts[ping_obj.id] = ping_obj
        return self.fill_list_of_hosts

    def dict_of_hosts_we_work_with(self):
        self.clear_list_of_hosts()
        data = read_current_hosts()
        for id_host in data:
            host = self.wwh.read_info_about_host(id_host)
            ping_obj = PingObject(
                host_id=host.host_id,
                ip_add=host.ip_add,
                name=host.name,
                music=host.music,
                description=host.descr,
            )
            self.list_of_hosts[id_host] = ping_obj

    def clear_list_of_hosts(self):
        self.list_of_hosts = {}

    def read_hosts_status(self):
        return self.list_of_hosts.values()

    def check_available_all_hosts_with_threading(self):
        self.mode_work = 'Threads'
        queue = Queue()
        threads = []
        for host in self.list_of_hosts.values():
            sleep(.3)
            t = Thread(target=handle_info_about_host,
                       args=(str(host.id), host.ip_add, queue))
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
        results = []
        while not queue.empty():
            results.append(queue.get())
        return results

    def check_available_all_hosts_with_async(self):
        self.mode_work = 'async'
        hosts = self.list_of_hosts.values()
        info_host = []
        for host in hosts:
            info_host.append((host.id, host.ip_add))
        result = run_ping(info_host)
        return result

    def check_available_all_hosts_with_os_func_async(self):
        self.mode_work = 'async_with_os_func'
        hosts = self.list_of_hosts.values()
        info_host = []
        for host in hosts:
            info_host.append((host.id, host.ip_add))
        (online_hosts, online_hosts_with_error,
         offline_hosts) = allocation_to_lists_async(info_host)
        for host in online_hosts:  # online host
            if host:
                self.what_do_when_online(int(host[0]), host[2])
        for host in online_hosts_with_error:  # online host with errors
            if host:
                self.what_do_when_online_with_errors(int(host[0]),
                                                     host[2],
                                                     host[3])
        for host in offline_hosts:  # offline host
            if host:
                self.what_do_when_offline(int(host[0]))

    def allocation_to_lists(self):
        result = self.check_available_all_hosts_with_threading()
        online_hosts = []
        online_hosts_with_error = []
        offline_hosts = []
        errors = []
        for res in result:
            if res[-1] == 'online':
                online_hosts.append(res)
            elif res[-1] == 'online_with_error':
                online_hosts_with_error.append(res)
            elif res[-1] == 'offline':
                offline_hosts.append(res)
            else:
                errors.append(res)
        return online_hosts, online_hosts_with_error, offline_hosts, errors

    def processing_lists(self):
        (online_hosts, online_hosts_with_error, offline_hosts,
         errors) = self.allocation_to_lists()
        for host in online_hosts:  # online host
            if host:
                average_delay = round((sum(host[2:5]) / 3), 4)
                self.what_do_when_online(int(host[0]), average_delay)
        for host in online_hosts_with_error:  # online host with errors
            if host:
                lost_packets = 0
                sum_delay = 0
                for i in host[2:5]:
                    # print(f'{host[2:5]=}')
                    if isinstance(i, float):
                        sum_delay += i
                    else:
                        lost_packets += 1
                average_delay = round((sum_delay / (3 - lost_packets)), 4)
                self.what_do_when_online_with_errors(int(host[0]),
                                                     average_delay,
                                                     lost_packets)
        for host in offline_hosts:  # offline host
            if host:
                self.what_do_when_offline(int(host[0]))
        if len(errors) != 0:  # errors
            app_loger.error('Проблемы с сетевой картой или кабелем')
            PyVoice.say_computer_about_cable()

    def what_do_when_online(self, host: int, delay: float):
        current_host = self.list_of_hosts.get(host)
        current_host.setup_average_delay(delay)
        if current_host.status_host == 'online_with_error':
            current_host.change_color('green')
            current_host.change_status_host_on_online()
        elif current_host.status_host in ('unknown', 'offline'):
            current_host.change_status_host_on_online()
            current_host.change_color('green')
            self.wwhs.create(current_host.id, current_host.status_host)
        self.list_of_hosts[current_host.id] = current_host

    def what_do_when_online_with_errors(self, host: int,
                                        delay: float,
                                        lost_pac: int):
        current_host = self.list_of_hosts.get(host)
        color = self.define_color(lost_pac)
        current_host.change_color(color)
        current_host.setup_average_delay(delay)
        if current_host.status_host in ('unknown', 'offline'):
            current_host.change_status_host_on_online()
            self.wwhs.create(current_host.id, current_host.status_host)
        elif current_host.status_host == 'online':
            current_host.change_status_host_on_online_with_errors()
        self.wwlp.create(current_host.id, lost_pac)
        self.list_of_hosts[current_host.id] = current_host

    def what_do_when_offline(self, host: int):
        current_host = self.list_of_hosts.get(host)
        if current_host.status_host in ('unknown', 'online',
                                        'online_with_error'):
            current_host.change_status_host_on_offline()
            current_host.change_color('red')
            self.list_of_hosts[current_host.id] = current_host
            self.wwhs.create(current_host.id, current_host.status_host)
        self.play_alarm(current_host)

    @staticmethod
    def define_color(amount_lp: int) -> str:
        if amount_lp == 1:
            return 'yellow'
        else:
            return 'orange'

    @staticmethod
    def play_alarm(host):
        try:
            if host.engine_sound:
                PyVoice.say_computer(host.name)
            else:
                playsound(f'program_voice/voice_files/{host.alarm}')
        except Exception as e:
            app_loger.critical(f'play_alarm:{e}')


if __name__ == "__main__":
    manager = Manager()
    # manager.add_all_hosts()
    # print(manager.check_available_all_hosts_with_os_func_async())
    # PyVoice.say_computer_about_cable()
    manager.dict_of_hosts_we_work_with()
    data1 = manager.read_hosts_status()
    manager.clear_list_of_hosts()
    manager.add_all_hosts()
    data2 = manager.read_hosts_status()
    print(data1)
    print(data2)
    print(data1 == data2)


# so cool!
