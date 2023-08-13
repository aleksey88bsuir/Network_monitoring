# pyuic5 name.ui -o name.py
from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QTableWidgetItem, QDesktopWidget, QSizePolicy
from ui.main_window import Ui_MainWindow
from run_nm_for_gui import Monitoring
from manager import Manager
from ui.skins.skins import blue_dark
from program_voice.python_voice import PyVoice
from loger import app_loger


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.step = 0
        self.manager = Manager()
        self.ui.retranslateUi(self)
        self.monitoring = Monitoring(self)
        self.monitor_height = QDesktopWidget().screenGeometry().height()
        self.set_data()
        self.start_interface()
        self.setStyleSheet(blue_dark)
        self.hosts_data = None
        self.start_program = None

    def start_interface(self):
        self.ui.b_start.clicked.connect(self.start_monitoring)
        self.ui.b_stop.clicked.connect(self.stop_monitoring)
        self.ui.b_stop.setEnabled(False)
        self.ui.b_modify.clicked.connect(self.open_modify_window)
        self.ui.q_volume_cont.setRange(0, 100)
        self.ui.q_volume_cont.setValue(70)
        self.ui.q_volume_cont.setNotchesVisible(True)
        self.ui.q_volume_cont.valueChanged.connect(self.set_volume_level)
        self.ui.l_volume.setText('Уровень громкости: 70 %')

    def set_data(self):
        self.manager.add_host()
        self.hosts_data = self.manager.read_hosts_status()
        self.ui.tableWidget.setRowCount(len(self.hosts_data))
        self.ui.tableWidget.setSizePolicy(QSizePolicy.Expanding,
                                          QSizePolicy.Expanding)
        self.refresh_table()

    def set_volume_level(self):
        level = self.ui.q_volume_cont.value()
        self.ui.l_volume.setText(f'Уровень громкости: {level} %')
        PyVoice.volume_level = level/100

    def refresh_table(self):
        self.hosts_data = self.manager.read_hosts_status()
        for i, string in enumerate(self.hosts_data):
            self.ui.tableWidget.setItem(i, 0,
                                        self.set_item_in_table(string,
                                                               'name'))
            self.ui.tableWidget.setItem(i, 1,
                                        self.set_item_in_table(string,
                                                               'ip_add'))
            self.ui.tableWidget.setItem(i, 2,
                                        self.set_item_in_table(string,
                                                               'status_host'))
            self.ui.tableWidget.setItem(i, 3,
                                        self.set_item_in_table(string,
                                                               'average_delay')
                                        )
            self.ui.tableWidget.setItem(i, 4,
                                        self.set_item_in_table(string,
                                                               'descr')
                                        )
        self.step += 1

    @staticmethod
    def set_item_in_table(host, host_atr):
        item = QTableWidgetItem(f"{getattr(host, host_atr)}")
        item.setForeground(QBrush(QColor(host.color)))
        return item

    def start_monitoring(self):
        self.step = 1
        self.monitoring.run_program = True
        self.ui.b_start.setEnabled(False)
        self.ui.b_modify.setEnabled(False)
        self.ui.b_stop.setEnabled(True)
        self.monitoring.start()
        self.update_status(f'Программа запущена. Продолжительность цикла до'
                           f' 13 секунд. Шаг №  {self.step}')

    def update_status(self, text):
        self.ui.statusbar.showMessage(text)

    def stop_monitoring(self):
        self.monitoring.run_program = False
        self.ui.b_stop.setEnabled(False)
        self.update_status('Программа останавливается. Пожалуйста ожидайте')

    def open_modify_window(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    app.exec()
