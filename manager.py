from network_monitoring import handle_info_about_host
from db.work_with_table_hosts import WorkWithHosts
from db.work_with_table_inf_host import WorkWithHostStatus
from db.work_with_table_lp import WorkWithLostPackets
from ping_object import PingObject
from queue import Queue
from threading import Thread
from loger import app_loger
from program_voice.python_voice import say_computer, say_computer_about_cable


class Manager:
    """Класс управления программой"""
    def __init__(self):
        self.wwh = WorkWithHosts()
        self.wwhs = WorkWithHostStatus()
        self.wwlp = WorkWithLostPackets()
        self.list_of_hosts = {}

    def add_host(self) -> None:
        data_from_db = self.wwh.read_all_data()
        for data_about_host in data_from_db:
            ping_obj = PingObject(
                host_id=data_about_host.host_id,
                ip_add=data_about_host.ip_add,
                name=data_about_host.name,
                music=data_about_host.music,
                description=data_about_host.descr,
            )
            self.list_of_hosts[ping_obj.id] = ping_obj

    def clear_list_of_hosts(self):
        self.list_of_hosts = {}

    def read_hosts_status(self):
        return self.list_of_hosts.values()

    def check_available_all_hosts_with_threading(self):
        queue = Queue()
        threads = []
        for host in self.list_of_hosts.values():
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

    def allocation_to_lists(self):
        result = self.check_available_all_hosts_with_threading()
        print(result)
        online_hosts = []
        online_hosts_with_error = []
        offline_hosts = []
        errors = []
        for res in result:
            if res[0] == 0:
                online_hosts.append(res)
            elif res[0] == 1:
                online_hosts_with_error.append(res)
            elif res[0] == 2:
                offline_hosts.append(res)
            else:
                errors.append(res)
        return online_hosts, online_hosts_with_error, offline_hosts, errors

    def processing_lists(self):
        lists = self.allocation_to_lists()
        for host in lists[0]:  # online host
            if host:
                self.what_do_when_online(int(host[1]), host[3])
        for host in lists[1]:  # online host with errors
            if host:
                self.what_do_when_online_with_errors(int(host[1]), host[3],
                                                     host[4])
        for host in lists[2]:  # offline host
            if host:
                self.what_do_when_offline(int(host[1]))
        if len(lists[3]) != 0:  # errors
            app_loger.error('Проблемы с сетевой картой или кабелем')
            say_computer_about_cable()

    def what_do_when_online(self, host: int, delay: float):
        current_host = self.list_of_hosts.get(host)
        if current_host.status_host in ('unknown', 'offline'):
            current_host.change_status_host_on_online()
            current_host.change_color('green')
            current_host.setup_average_delay(delay)
            self.list_of_hosts[current_host.id] = current_host
            self.wwhs.create(current_host.id, current_host.status_host)

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
        self.wwlp.create(current_host.id, lost_pac)
        self.list_of_hosts[current_host.id] = current_host

    def what_do_when_offline(self, host: int):
        current_host = self.list_of_hosts.get(host)
        if current_host.status_host in ('unknown', 'online'):
            current_host.change_status_host_on_offline()
            current_host.change_color('red')
            self.list_of_hosts[current_host.id] = current_host
            self.wwhs.create(current_host.id, current_host.status_host)
            self.play_alarm(current_host)

    @staticmethod
    def define_color(amount_lp: int) -> str:
        if amount_lp == 1:
            return 'dark_yellow'
        else:
            return 'yellow'

    def play_alarm(self, host):
        pass

    def start_program(self):
        pass


def read_data():
    data = manager.read_hosts_status()
    for i in data:
        print(i)
    print('+'*60)


if __name__ == "__main__":
    manager = Manager()
    manager.clear_list_of_hosts()
    read_data()
    manager.add_host()
    read_data()
    manager.processing_lists()
    read_data()
    manager.start_program()
