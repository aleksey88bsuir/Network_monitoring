from time import sleep
from PyQt5.QtCore import QThread
from loger import app_loger


class Monitoring(QThread):
    def __init__(self, app):
        QThread.__init__(self)
        self.run_program = True
        self.app = app

    def run(self):
        try:
            while self.run_program:
                sleep(0)  # сон между циклами
                self.start_monitoring()
            self.app.ui.b_start.setEnabled(True)
            self.app.ui.b_modify.setEnabled(True)
            self.app.update_status('Программа остановлена')
        except Exception as e:
            app_loger.critical(f'Monitoring ren:\n {e}')

    def start_monitoring(self):
        if self.app.mode == 'async':
            self.app.manager.check_available_all_hosts_with_os_func_async()
        else:
            self.app.manager.processing_lists()
        self.app.refresh_table()
        self.app.update_status(f'Программа запущена. '
                               f'Продолжительность цикла до'
                               f' 13 секунд. Шаг № {self.app.step}')
