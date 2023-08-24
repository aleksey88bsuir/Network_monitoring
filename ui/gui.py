# pyuic5 name.ui -o name.py
from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QSizePolicy, \
    QHeaderView
from ui.main_window import Ui_MainWindow
from run_nm_for_gui import Monitoring
from manager import Manager
from program_voice.python_voice import PyVoice
from PyQt5.QtCore import QFile, Qt
from ui.edit_and_view import EditAndViewWindow
# from loger import app_loger


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.style_sheet = None
        self.step = 0
        self.manager = Manager()
        self.ui.retranslateUi(self)
        self.monitoring = Monitoring(self)
        self.set_data()
        self.start_interface()
        self.edit_and_view_window = EditAndViewWindow(self)
        self.hosts_data = None
        self.start_program = None
        self.mode = None

    def start_interface(self):
        self.ui.b_start.clicked.connect(self.start_monitoring)
        self.ui.b_stop.clicked.connect(self.stop_monitoring)
        self.ui.b_stop.setEnabled(False)
        self.ui.b_modify.clicked.connect(self.open_modify_window)
        self.ui.q_volume_cont.setRange(0, 100)
        self.ui.q_volume_cont.setValue(70)
        self.ui.q_volume_cont.setNotchesVisible(True)
        self.ui.q_volume_cont.valueChanged.connect(self.set_volume_level)
        self.ui.l_volume.setText('70 %')
        for style_name, style_path in (
                self.get_css_files('ui/PyQt5_stylesheets').items()):
            self.ui.cd_style.addItem(style_name, style_path)
        self.ui.cd_style.currentTextChanged.connect(self.change_style)
        self.ui.cd_style.setCurrentIndex(4)
        self.change_style()
        self.ui.cb_mode_work.setCurrentIndex(0)
        pixmap = QPixmap('ui/pics_for_gui/r-443.png')
        self.ui.picture.setPixmap(pixmap)

    def set_data(self):
        self.manager.dict_of_hosts_we_work_with()
        # self.manager.add_all_hosts()
        self.hosts_data = self.manager.read_hosts_status()
        self.ui.tableWidget.setRowCount(len(self.hosts_data))
        self.refresh_table()

    def set_volume_level(self):
        level = self.ui.q_volume_cont.value()
        self.ui.l_volume.setText(f'{level} %')
        PyVoice.volume_level = level/100

    def refresh_table(self):
        self.hosts_data = self.manager.read_hosts_status()
        self.ui.tableWidget.setRowCount(len(self.hosts_data))
        print(self.hosts_data)
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
        self.ui.tableWidget.setSizePolicy(QSizePolicy.Expanding,
                                          QSizePolicy.Expanding)

        (self.ui.tableWidget.horizontalHeader().
         setSectionResizeMode(QHeaderView.ResizeToContents))

        (self.ui.tableWidget.verticalHeader().
         setSectionResizeMode(QHeaderView.ResizeToContents))

        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.step += 1

    @staticmethod
    def set_item_in_table(host, host_atr):
        item = QTableWidgetItem(f"{getattr(host, host_atr)}")
        item.setForeground(QBrush(QColor(host.color)))
        return item

    def start_monitoring(self):
        mode = self.ui.cb_mode_work.currentText()
        if mode == 'Многопоточный':
            self.mode = 'threads'
        else:
            self.mode = 'async'
        self.step = 1
        self.monitoring.run_program = True
        self.ui.b_start.setEnabled(False)
        self.ui.b_modify.setEnabled(False)
        self.ui.b_stop.setEnabled(True)
        self.monitoring.start()
        self.update_status(f'Программа запущена. Продолжительность цикла до'
                           f' 15 секунд. Шаг №  {self.step}')

        self.ui.cb_mode_work.setDisabled(True)

    def update_status(self, text):
        self.ui.statusbar.showMessage(text)

    def stop_monitoring(self):
        self.monitoring.run_program = False
        self.ui.b_stop.setEnabled(False)
        self.update_status('Программа останавливается. Пожалуйста ожидайте')
        self.ui.cb_mode_work.setDisabled(False)

    def change_style(self):
        file = QFile(self.ui.cd_style.currentData())
        file.open(QFile.ReadOnly | QFile.Text)
        stream = file.readAll()
        self.style_sheet = str(stream, encoding='utf-8')
        self.setStyleSheet(self.style_sheet)

    @staticmethod
    def get_css_files(folder):
        import os
        css_files = dict()
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".qss") or file.endswith(".css"):
                    css_files[file[6:-4].capitalize()] = os.path.join(root,
                                                                      file)
        return css_files

    def open_modify_window(self):
        self.edit_and_view_window.setWindowModality(Qt.ApplicationModal)
        self.edit_and_view_window.setWindowTitle('Окно редактирования '
                                                 '(просмотра) информации')
        self.edit_and_view_window.setStyleSheet(self.style_sheet)
        self.edit_and_view_window.init()
        self.edit_and_view_window.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    app.exec()
