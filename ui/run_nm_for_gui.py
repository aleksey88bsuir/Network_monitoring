import time
from PyQt5.QtCore import QThread
from loger import app_loger


class Monitoring(QThread):
    def __init__(self, app):
        QThread.__init__(self)
        self.run_program = True
        self.app = app

    def run(self):

        while self.run_program:
            self.start_monitoring()
            # time.sleep(.5)
        self.app.ui.b_start.setEnabled(True)
        self.app.ui.b_modify.setEnabled(True)
        self.app.update_status('Программа остановлена')
        # except Exception as e:
        #     print('run')
        #     print(e)
        #     app_loger.critical(e)

    def start_monitoring(self):
        # self.app.manager.mode_work = 'async'
        self.app.manager.mode_work = 'Threads'
        self.app.manager.mode_work = 'async_with_os_func'
        # self.app.manager.check_available_all_hosts_with_os_func_async()
        self.app.manager.processing_lists()
        self.app.refresh_table()
        self.app.update_status(f'Программа запущена. Продолжительность цикла до'
                           f' 13 секунд. Шаг № {self.app.step}')
