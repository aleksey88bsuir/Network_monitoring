from PyQt5.QtCore import QThread
from PyQt5 import QtWidgets
from loger import LoggerWrapper


class Monitoring(QThread):
    def __init__(self, app: QtWidgets) -> None:
        QThread.__init__(self)
        self.loger = LoggerWrapper()
        self.run_program = True
        self.app = app

    def run(self) -> None:
        try:
            while self.run_program:
                self.start_monitoring()
            self.app.ui.b_start.setEnabled(True)
            self.app.ui.b_modify.setEnabled(True)
            self.app.update_status('Программа остановлена')
        except Exception as e:
            self.loger.log_error(e)

    def start_monitoring(self) -> None:
        try:
            if self.app.mode == 'async':
                self.app.manager.check_available_all_hosts_with_os_func_async()
            else:
                self.app.manager.processing_lists()
            self.app.refresh_table()
            self.app.update_status(f'Программа запущена. '
                                   f'Продолжительность цикла до'
                                   f' 13 секунд. Шаг № {self.app.step}')
        except Exception as e:
            self.loger.log_error(e)
