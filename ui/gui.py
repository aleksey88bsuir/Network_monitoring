from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from ui.main_window import Ui_MainWindow
from run_nm_for_gui import Monitoring
from manager import Manager


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.manager = Manager()
        self.ui.retranslateUi(self)
        self.monitoring = Monitoring(self)
        self.set_data()
        self.start_interface()
        self.hosts_data = None
        self.start_program = None

    def start_interface(self):
        self.ui.b_start.clicked.connect(self.start_monitoring)
        self.ui.b_stop.clicked.connect(self.stop_monitoring)
        self.ui.b_stop.setEnabled(False)

    def set_data(self):
        self.manager.add_host()
        self.hosts_data = self.manager.read_hosts_status()
        self.ui.tableWidget.setRowCount(len(self.hosts_data))
        self.refresh_table()

    def refresh_table(self):
        self.hosts_data = self.manager.read_hosts_status()
        for i, string in enumerate(self.hosts_data):
            self.ui.tableWidget.setItem(i, 0, self.set_item(string, 'name'))
            self.ui.tableWidget.setItem(i, 1, self.set_item(string, 'ip_add'))
            self.ui.tableWidget.setItem(i, 2,
                                        self.set_item(string, 'status_host'))
            self.ui.tableWidget.setItem(i, 3,
                                        self.set_item(string, 'average_delay'))
            self.ui.tableWidget.setItem(i, 4,
                                        self.set_item(string, 'descr'))
            self.ui.tableWidget.resizeColumnsToContents()

    @staticmethod
    def set_item(host, host_atr):
        item = QTableWidgetItem(f"{getattr(host, host_atr)}")
        item.setForeground(QBrush(QColor(host.color)))
        return item

    def start_monitoring(self):
        self.monitoring.run_program = True
        self.ui.b_start.setEnabled(False)
        self.ui.b_stop.setEnabled(True)
        self.monitoring.start()

    def stop_monitoring(self):
        self.monitoring.run_program = False
        self.ui.b_stop.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    app.exec()
