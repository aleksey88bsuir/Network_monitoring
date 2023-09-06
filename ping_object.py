import datetime


class PingObject:

    def __init__(self, host_id: int, ip_add: str,
                 name: str, music: str = '', description: str = '') -> None:
        self.id = host_id
        self.name = name
        self.ip_add = ip_add
        self.alarm = music
        self.descr = description
        self.average_delay = None
        self.status_host = 'unknown'
        self.color = 'gray'
        self.engine_sound = "engine_sound" if self.alarm == '' else None
        self.delay_and_time_list = list()

    def change_status_host_on_online(self) -> None:
        self.status_host = 'online'

    def change_status_host_on_online_with_errors(self) -> None:
        self.status_host = 'online_with_error'

    def change_status_host_on_offline(self) -> None:
        self.status_host = 'offline'

    def change_color(self, color: str) -> None:
        self.color = color

    def setup_average_delay(self, delay: float) -> None:
        self.average_delay = delay

    def add_delay_and_time(
            self,
            delay_and_time: tuple[float,  datetime]) -> None:
        self.delay_and_time_list.append(delay_and_time)

    def get_delay_and_time(self) -> tuple:
        return tuple(self.delay_and_time_list)

    def __str__(self) -> str:
        return f'{self.id} -- {self.name} -- {self.ip_add} -- {self.descr}'
