# pyuic5 name.ui -o name.py
from PyQt5 import QtWidgets
from PyQt5.QtGui import QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QSizePolicy, \
    QHeaderView, QMessageBox
from ui.main_window import Ui_MainWindow
from run_nm_for_gui import Monitoring
from func_for_gui import get_music_file
from manager import Manager
from program_voice.python_voice import PyVoice
from PyQt5.QtCore import QFile, Qt
from ui.edit_and_view import EditAndViewWindow
from loger import LoggerWrapper, app_loger, log_exceptions
from ping_object import PingObject


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.log = LoggerWrapper()
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
        self.write_successful_message()

    def write_successful_message(self) -> None:
        self.log.log_info('Программа успешно запущена')

    def start_interface(self) -> None:
        try:
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
        except Exception as e:
            self.loger.log_error(e)

    def set_data(self) -> None:
        try:
            self.manager.dict_of_hosts_we_work_with()
            self.hosts_data = self.manager.read_hosts_status()
            self.ui.tableWidget.setEditTriggers(
                QtWidgets.QAbstractItemView.NoEditTriggers)
            self.refresh_table()
        except Exception as e:
            self.loger.log_error(e)

    def set_volume_level(self) -> None:
        try:
            level = self.ui.q_volume_cont.value()
            self.ui.l_volume.setText(f'{level} %')
            PyVoice.volume_level = level/100
        except Exception as e:
            self.loger.log_error(e)

    def refresh_table(self) -> None:
        try:
            self.hosts_data = self.manager.read_hosts_status()
            self.ui.tableWidget.setRowCount(len(self.hosts_data))
            for i, host in enumerate(self.hosts_data):
                self.ui.tableWidget.setItem(i, 0,
                                            self.set_item_in_table(host,
                                                                   'name'))
                self.ui.tableWidget.setItem(i, 1,
                                            self.set_item_in_table(host,
                                                                   'ip_add'))
                self.ui.tableWidget.setItem(i, 2,
                                            self.set_item_in_table(
                                                host, 'status_host'))
                self.ui.tableWidget.setItem(i, 3,
                                            self.set_item_in_table(
                                                host, 'average_delay')
                                            )
                self.ui.tableWidget.setItem(i, 4,
                                            self.set_item_in_table(host,
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
        except Exception as e:
            self.loger.log_error(e)

    @staticmethod
    @log_exceptions(logger=app_loger)
    def set_item_in_table(host: PingObject, host_atr: str) -> QTableWidgetItem:
        item = QTableWidgetItem(f"{getattr(host, host_atr)}")
        item.setForeground(QBrush(QColor(host.color)))
        return item

    def start_monitoring(self) -> None:
        try:
            if self.__can_start():
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
                self.update_status(f'Программа запущена. '
                                   f'Продолжительность цикла '
                                   f'до 15 секунд. Шаг №  {self.step}')
                self.ui.cb_mode_work.setDisabled(True)
                self.log.log_info('Старт мониторинга хостов')
        except Exception as e:
            self.log.log_error(e)

    def update_status(self, text: str) -> None:
        try:
            self.ui.statusbar.showMessage(text)
        except Exception as e:
            self.log.log_error(e)

    def stop_monitoring(self) -> None:
        try:
            self.monitoring.run_program = False
            self.ui.b_stop.setEnabled(False)
            self.update_status('Программа останавливается. '
                               'Пожалуйста ожидайте')
            self.ui.cb_mode_work.setDisabled(False)
            self.log.log_info('Мониторинг хостов успешно завершен')
        except Exception as e:
            self.log.log_error(e)

    def change_style(self) -> None:
        try:
            file = QFile(self.ui.cd_style.currentData())
            file.open(QFile.ReadOnly | QFile.Text)
            stream = file.readAll()
            self.style_sheet = str(stream, encoding='utf-8')
            self.setStyleSheet(self.style_sheet)
        except Exception as e:
            self.log.log_error(e)

    @staticmethod
    @log_exceptions(logger=app_loger)
    def get_css_files(folder: str) -> dict:
        import os
        css_files = dict()
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".qss") or file.endswith(".css"):
                    css_files[file[6:-4].capitalize()] = os.path.join(root,
                                                                      file)
        return css_files

    def open_modify_window(self) -> None:
        try:
            self.edit_and_view_window.setWindowModality(Qt.ApplicationModal)
            self.edit_and_view_window.setWindowTitle('Окно редактирования '
                                                     '(просмотра) информации')
            self.edit_and_view_window.setStyleSheet(self.style_sheet)
            self.edit_and_view_window.clear_setting_data()
            self.edit_and_view_window.init()
            self.edit_and_view_window.show()
        except Exception as e:
            self.log.log_error(e)

    def __can_start(self) -> bool:
        try:
            hosts = self.manager.read_hosts_status()
            if len(hosts) == 0:
                QMessageBox.information(self,
                                        "Программа не может быть запущена!!!",
                                        "Необходимо выбрать хотя бы 1 хост")
                return False
            music_files = get_music_file('program_voice/voice_files/')
            for host in hosts:
                if host.alarm not in music_files:
                    QMessageBox.information(
                        self,
                        "Программа не может быть запущена!!!",
                        f"Отсутствует музыкальный файл \n"
                        f"{host.alarm} y хоста {host.name} в"
                        f"папке с музыкой. Измените данные"
                        )
                    return False
            return True
        except Exception as e:
            self.log.log_error(e)

    def closeEvent(self, event):
        close = QMessageBox.question(
            self, "Выход из программы",
            "Вы уверены, что хотите закрыть программу сетевого мониторинга?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if close == QMessageBox.Yes:
            self.log.log_info('Программа закрыта пользователем')
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    app.exec()
