import time
from PyQt5.QtCore import QThread


class Monitoring(QThread):
    def __init__(self, app):
        QThread.__init__(self)
        self.run_program = True
        self.app = app
        self.start_monitoring()

    def run(self):
        while self.run_program:
            self.start_monitoring()
            time.sleep(1)
            print('New circle')
        print('Stop program')
        self.app.ui.b_start.setEnabled(True)

    def start_monitoring(self):
        self.app.manager.processing_lists()
        self.app.refresh_table()
