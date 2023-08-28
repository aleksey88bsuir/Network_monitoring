from PyQt5 import QtWidgets

from ui.add_and_edit_window import Ui_Dialog


class AddAndEditWindow(QtWidgets.QDialog):
    def __init__(self, edit_and_view_window):
        super().__init__()
        self.edit_and_view_window = edit_and_view_window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    def init(self):
        self.start_interface()
        self.set_data()
        self.all_update()

    def all_update(self):
        pass

    def start_interface(self):
        self.ui.b_ok.clicked.connect(self.add_host)
        self.ui.b_cancel.clicked.connect(self.close_window)
        self.ui.alarm_edit.setDisabled(True)

    def set_data(self):
        pass

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

    def __validate_ip_add(self, ip_add: str) -> bool:
        if not self.ui.checkBox.isChecked():
            import re
            self.ui.l_warning_ip_add.setText('Проверьте правильность ввода'
                                                     'IP aдреса')
        return True

    def __validate_name(self, host_name: str) -> bool:
        return True

    def close_window(self):
        self.ui.ip_add_edit.setText('')
        self.ui.name_edit.setText('')
        self.ui.alarm_edit.setText('')
        self.ui.descr_edit.setText('')
        self.close()
