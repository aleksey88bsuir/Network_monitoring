from PyQt5 import QtWidgets
from ui.add_and_edit_window import Ui_Dialog
from func_for_gui import get_music_file
from manager import Manager


class AddAndEditWindow(QtWidgets.QDialog):
    def __init__(self, edit_and_view_window):
        super().__init__()
        self.edit_and_view_window = edit_and_view_window
        self.edit_host = None
        self.music_files = get_music_file('program_voice/voice_files/')
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.manager = Manager()
        self.hosts_name = [host.name for host
                           in self.manager.read_all_hosts().values()]
        self.hosts_ip_add = [str(host.ip_add) for host
                             in self.manager.read_all_hosts().values()]
        for music_name in self.music_files:
            self.ui.alarm_edit.addItem(music_name)
        self.ui.b_cancel.clicked.connect(self.close_window)

    def init_add_host(self):
        self.default_setting()
        self.ui.b_ok.clicked.connect(self.add_host)

    def init_edit_host(self, host_id):
        self.default_setting()
        self.edit_host = (self.edit_and_view_window.main_window.manager.wwh.
                read_info_about_host(host_id))
        if self.edit_host:
            self.ui.ip_add_edit.setText(self.edit_host.ip_add)
            self.ui.name_edit.setText(self.edit_host.name)
            if index := self.music_files.index(self.edit_host.music):
                self.ui.alarm_edit.setCurrentIndex(index)
            self.ui.descr_edit.setText(self.edit_host.descr)
            self.ui.b_ok.clicked.connect(self.update_host)

    def add_host(self):
        ip_add = self.ui.ip_add_edit.text()
        host_name = self.ui.name_edit.text()
        alarm = self.ui.alarm_edit.currentText()
        descr = self.ui.descr_edit.toPlainText()
        if self.__validate_ip_add(ip_add) and self.__validate_name(host_name):
            self.edit_and_view_window.main_window.manager.wwh.create(
                {'ip_add': ip_add,
                 'name': host_name,
                 'music': alarm,
                 'descr': descr}
            )
            self.hosts_name.append(host_name)
            self.hosts_ip_add.append(ip_add)
            self.edit_and_view_window.clear_setting_data()
            self.edit_and_view_window.set_data()
            self.edit_and_view_window.all_update()
            self.default_setting()
            self.close()

    def update_host(self):
        self.hosts_name.remove(self.edit_host.name)
        self.hosts_ip_add.remove(self.edit_host.ip_add)
        ip_add = self.ui.ip_add_edit.text()
        host_name = self.ui.name_edit.text()
        alarm = self.ui.alarm_edit.currentText()
        descr = self.ui.descr_edit.toPlainText()
        if (self.__validate_ip_add(ip_add) and
                self.__validate_name(host_name)):
            self.edit_host.ip_add = ip_add
            self.edit_host.name = host_name
            self.edit_host.music = alarm
            self.edit_host.descr = descr
            self.edit_and_view_window.main_window.manager.wwh.update_host(
                self.edit_host)
            self.hosts_ip_add.append(ip_add)
            self.hosts_name.append(host_name)
            self.edit_and_view_window.clear_setting_data()
            self.edit_and_view_window.set_data()
            self.edit_and_view_window.all_update()
            self.edit_and_view_window.save_changes()
            self.close()
        else:
            self.hosts_name.append(self.edit_host.name)
            self.hosts_ip_add.append(self.edit_host.ip_add)

    def __validate_ip_add(self, ip_add: str) -> bool:
        self.ui.l_warning_ip_add.clear()
        self.ui.l_warning_ip_add.setStyleSheet("color: red")
        if not ip_add:
            self.ui.l_warning_ip_add.setText('Введите ip адрес')
            return False
        if not self.ui.checkBox.isChecked():
            import re
            regex = (r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)'
                     r'{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
            if not re.match(regex, ip_add):
                self.ui.l_warning_ip_add.setText('Проверьте '
                                                     'IP aдрес')
                return False

            if ip_add in self.hosts_ip_add:
                self.ui.l_warning_ip_add.setText('Хост с таким ip '
                                                 'уже существует')
                return False
        return True

    def __validate_name(self, host_name: str) -> bool:
        self.ui.l_warning_name.clear()
        self.ui.l_warning_name.setStyleSheet("color: red")
        if not host_name:
            self.ui.l_warning_name.setText('Введите имя')
            return False
        if host_name in self.hosts_name:
            self.ui.l_warning_name.setText('Хост с таким именем '
                                             'уже существует')
            return False
        return True

    def close_window(self):
        self.default_setting()
        self.close()

    def default_setting(self):
        self.ui.ip_add_edit.setText('')
        self.ui.name_edit.setText('')
        self.ui.descr_edit.setText('')
        self.ui.alarm_edit.setCurrentIndex(0)
        self.ui.l_warning_name.setText('')
        self.ui.l_warning_ip_add.setText('')
