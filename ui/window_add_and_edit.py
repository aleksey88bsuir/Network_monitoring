from PyQt5 import QtWidgets
from ui.add_and_edit_window import Ui_Dialog


class AddAndEditWindow(QtWidgets.QDialog):
    def __init__(self, edit_and_view_window):
        super().__init__()
        self.edit_and_view_window = edit_and_view_window
        self.edit_host = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    def init_add_host(self):
        self.default_setting()
        self.ui.b_ok.clicked.connect(self.add_host)
        self.start_interface()

    def init_edit_host(self, host_id):
        self.default_setting()
        self.edit_host = (self.edit_and_view_window.main_window.manager.wwh.
                read_info_about_host(host_id))
        self.ui.ip_add_edit.setText(self.edit_host.ip_add)
        self.ui.name_edit.setText(self.edit_host.name)
        self.ui.alarm_edit.setText(self.edit_host.music)
        self.ui.descr_edit.setText(self.edit_host.descr)
        self.ui.b_ok.clicked.connect(self.update_host)

    def start_interface(self):
        self.ui.b_cancel.clicked.connect(self.close_window)
        self.ui.alarm_edit.setDisabled(True)

    def add_host(self):
        ip_add = self.ui.ip_add_edit.text()
        host_name = self.ui.name_edit.text()
        alarm = self.ui.alarm_edit.text()
        descr = self.ui.descr_edit.toPlainText()
        if self.__validate_ip_add(ip_add) and self.__validate_name(host_name):
            self.edit_and_view_window.main_window.manager.wwh.create(
                {'ip_add': ip_add,
                 'name': host_name,
                 'music': alarm,
                 'descr': descr}
            )
            self.close()
            self.edit_and_view_window.clear_setting_data()
            self.edit_and_view_window.set_data()
            self.edit_and_view_window.all_update()

    def update_host(self):
        ip_add = self.ui.ip_add_edit.text()
        host_name = self.ui.name_edit.text()
        alarm = self.ui.alarm_edit.text()
        descr = self.ui.descr_edit.toPlainText()
        if self.__validate_ip_add(ip_add) and self.__validate_name(host_name):
            self.edit_host.ip_add = ip_add
            self.edit_host.name = host_name
            self.edit_host.music = alarm
            self.edit_host.descr = descr
            self.edit_and_view_window.main_window.manager.wwh.update_host(
                self.edit_host)
            self.close()
            self.edit_and_view_window.clear_setting_data()
            self.edit_and_view_window.set_data()
            self.edit_and_view_window.all_update()
            self.edit_and_view_window.save_changes()

    def __validate_ip_add(self, ip_add: str) -> bool:
        if not self.ui.checkBox.isChecked():
            import re
            self.ui.l_warning_ip_add.setText('Проверьте правильность ввода'
                                                     'IP aдреса')
        return True

    def __validate_name(self, host_name: str) -> bool:
        return True

    def close_window(self):
        self.default_setting()
        self.close()

    def default_setting(self):
        self.ui.ip_add_edit.clear()
        self.ui.name_edit.clear()
        self.ui.alarm_edit.clear()
        self.ui.descr_edit.clear()
        self.ui.l_warning_name.clear()
        self.ui.l_warning_ip_add.clear()
