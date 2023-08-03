class PingObject:

    def __init__(self, host_id, ip_add, name, music='', description=''):
        self.id = host_id
        self.name = name
        self.ip_add = ip_add
        self.alarm = music
        self.descr = description
        self.status_host = 'unknown'
        self.color = 'gray'
        self.host_alarm = music
        if self.host_alarm == '':
            self.engine_sound = "engine_sound"
        else:
            self.engine_sound = None

    def change_status_host_on_online(self):
        self.status_host = 'online'

    def change_status_host_on_offline(self):
        self.status_host = 'offline'

    def change_color(self, color: str):
        self.color = color

    def __str__(self):
        return f'Объект с атрибутами: {self.__dict__}'
