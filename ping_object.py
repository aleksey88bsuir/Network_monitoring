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
        if self.alarm == '':
            self.engine_sound = "engine_sound"
        else:
            self.engine_sound = None

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

    def __str__(self) -> str:
        return f'{self.id} -- {self.name} -- {self.ip_add} -- {self.descr}'
