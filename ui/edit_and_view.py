from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem, QHeaderView, \
    QSizePolicy
from ui.edit_and_view_window import Ui_Dialog
from search_host import HostsIter
from list_of_hosts_we_work_with import write_current_hosts
from window_add_and_edit import AddAndEditWindow
from func_for_gui import (show_host_status_history,
                          show_host_status_history_with_time)


class EditAndViewWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.access_hosts = None
        self.working_hosts = None
        self.all_hosts = None
        self.current_hosts = None
        self.id_host_in_table = None
        self.list_with_id_hosts = []
        self.hosts_iter_first_window = HostsIter()
        self.hosts_iter_second_window = HostsIter()
        self.hosts_iter_third_window = HostsIter()
        self.window_add_and_edit = AddAndEditWindow(self)

    def init(self):
        self.start_interface()
        self.set_data()
        self.all_update()

    def all_update(self):
        self.update_date_in_tables_on_first_window()
        self.update_date_in_tables_on_second_window()
        self.update_date_in_tables_on_third_window()
        self.update_buttons_on_first_window()
        self.update_buttons_on_second_window()
        self.update_buttons_on_third_window()

    def start_interface(self):
        self.ui.tabWidget.setTabText(0, "Выбор хостов для работы")
        self.ui.tabWidget.setTabText(1, "Информация о хостах")
        self.ui.tabWidget.setTabText(2, "Редактор таблицы")
        self.ui.search_line.textChanged.connect(self.parse_first_window)
        self.ui.search_edit_2.textChanged.connect(self.parse_second_window)
        self.ui.search_line_2.textChanged.connect(self.parse_third_window)

        self.ui.list_access_hosts.itemSelectionChanged.connect(
            self.handle_selection_change_access_list)
        self.ui.list_working_hosts.itemSelectionChanged.connect(
            self.handle_selection_change_work_list)
        self.ui.list_with_access_hosts2.itemSelectionChanged.connect(
            self.handle_selection_access_list2)

        self.ui.b_up.clicked.connect(self.move_up)
        self.ui.b_down.clicked.connect(self.move_down)
        self.ui.b_save_changes.clicked.connect(self.save_changes)
        self.ui.b_add.clicked.connect(self.add_host)
        self.ui.b_del.clicked.connect(self.del_host)
        self.ui.b_edit.clicked.connect(self.edit_host)
        self.ui.b_read_history_connection.clicked.connect(
            self.read_history_connection)
        self.ui.b_read_history_lp.clicked.connect(self.read_history_lp)
        self.ui.b_view_packet_delay_graph.clicked.connect(
            self.view_packet_delay_graph)

        self.ui.t_all_hosts.cellClicked.connect(self.handle_cell_clicked)
        self.ui.t_all_hosts.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.b_save_changes.setDisabled(True)
        self.update_buttons_on_first_window()
        self.update_buttons_on_second_window()
        self.update_buttons_on_third_window()

    def set_data(self):
        self.all_hosts = self.main_window.manager.read_all_hosts().values()

        self.access_hosts = \
            [str(host) for host
             in self.all_hosts]
        self.working_hosts = \
            [str(host) for host
             in self.main_window.manager.read_hosts_status()]

        for host in self.working_hosts:
            self.list_with_id_hosts.append(self.get_id_host(host))

        for host in self.access_hosts:
            self.hosts_iter_third_window.add_new_host(host)

        self.current_hosts = self.all_hosts

    def clear_setting_data(self):
        self.hosts_iter_first_window.clear()
        self.hosts_iter_second_window.clear()
        self.hosts_iter_third_window.clear()
        self.ui.search_line.clear()
        self.ui.search_line_2.clear()
        self.ui.search_edit_2.clear()
        self.access_hosts = None
        self.working_hosts = None
        self.all_hosts = None
        self.current_hosts = None
        self.id_host_in_table = None
        self.list_with_id_hosts = []

    @staticmethod
    def get_id_host(info_string):
        import re
        ip_add_pattern = r'(\d+) --'
        host_id_ = re.findall(ip_add_pattern, info_string)[0]
        return host_id_

# _________first_window____________________________

    def update_date_in_tables_on_first_window(self):
        self.ui.list_access_hosts.clear()
        self.ui.list_working_hosts.clear()
        self.hosts_iter_first_window.clear()
        for host in self.access_hosts:
            self.hosts_iter_first_window.add_new_host(str(host))
            self.ui.list_access_hosts.addItem(QListWidgetItem(str(host)))
        for host in self.working_hosts:
            self.ui.list_working_hosts.addItem(QListWidgetItem(str(host)))

    def update_data_in_table_working_hosts(self):
        self.ui.list_working_hosts.clear()
        for host in self.working_hosts:
            self.ui.list_working_hosts.addItem(QListWidgetItem(str(host)))

    def parse_first_window(self, char):
        self.ui.list_access_hosts.clear()
        data = []
        for item in self.hosts_iter_first_window:
            if char.lower() in item.lower():
                data.append(item)
        for string_item in data:
            item_ = QListWidgetItem(string_item)
            self.ui.list_access_hosts.addItem(item_)

    def handle_selection_change_access_list(self):
        self.selected_item = self.ui.list_access_hosts.currentItem()
        self.update_buttons_on_first_window()
        self.ui.b_down.setDisabled(False)

    def handle_selection_change_work_list(self):
        self.selected_item = self.ui.list_working_hosts.currentItem()
        self.update_buttons_on_first_window()
        self.ui.b_up.setDisabled(False)

    def update_buttons_on_first_window(self):
        self.ui.b_down.setDisabled(True)
        self.ui.b_up.setDisabled(True)

    def move_up(self):
        item = None
        try:
            try:
                item = self.selected_item.text()
            except AttributeError:
                print('Так нельзя делать')
            if item:
                self.host_id = self.get_id_host(item)
                if self.host_id:
                    self.list_with_id_hosts.remove(self.host_id)
                    self.working_hosts.remove(self.selected_item.text())
                    self.update_date_in_tables_on_first_window()
                    self.update_buttons_on_first_window()
                    self.ui.b_save_changes.setDisabled(False)
                    self.ui.search_line.clear()
        except RuntimeError:
            print('error')

    def move_down(self):
        try:
            self.host_id = self.get_id_host(self.selected_item.text())
            if self.host_id:
                if self.host_id not in self.list_with_id_hosts:
                    self.list_with_id_hosts.append(self.host_id)
                    self.working_hosts.append(self.selected_item.text())
                if self.ui.search_line.text():
                    self.update_data_in_table_working_hosts()
                else:
                    self.update_date_in_tables_on_first_window()
                self.update_buttons_on_first_window()
                self.ui.b_save_changes.setDisabled(False)
        except RuntimeError:
            print('RuntimeError: wrapped C/C++ object of type QListWidgetItem'
                  ' has been deleted')

    def save_changes(self):
        write_current_hosts(self.list_with_id_hosts)
        self.ui.b_save_changes.setDisabled(True)
        self.main_window.manager.dict_of_hosts_we_work_with()
        self.main_window.refresh_table()

# _________second_window____________________________
    def update_buttons_on_second_window(self):
        self.ui.b_read_history_connection.setDisabled(True)
        self.ui.b_read_history_lp.setDisabled(True)
        self.ui.b_view_packet_delay_graph.setDisabled(True)

    def update_date_in_tables_on_second_window(self):
        self.ui.list_with_access_hosts2.clear()
        for host in self.access_hosts:
            self.hosts_iter_second_window.add_new_host(str(host))
            self.ui.list_with_access_hosts2.addItem(QListWidgetItem(str(host)))

    def parse_second_window(self, char):
        self.ui.list_with_access_hosts2.clear()
        data = []
        for item in self.hosts_iter_second_window:
            if char.lower() in item.lower():
                data.append(item)
        for string_item in data:
            item_ = QListWidgetItem(string_item)
            self.ui.list_with_access_hosts2.addItem(item_)

    def handle_selection_access_list2(self):
        self.id_host_in_access_list2 = self.get_id_host(
            self.ui.list_with_access_hosts2.currentItem().text())
        self.ui.b_read_history_connection.setDisabled(False)
        self.ui.b_read_history_lp.setDisabled(False)
        self.ui.b_view_packet_delay_graph.setDisabled(False)

    def read_history_connection(self):
        if self.ui.time_filter.isChecked():
            start_time = self.ui.start_date_and_time.dateTime().toPyDateTime()
            end_time = self.ui.finish_date_and_time.dateTime().toPyDateTime()
            show_host_status_history_with_time(
                self.id_host_in_access_list2,
                start_time,
                end_time
            )
        else:
            show_host_status_history(self.id_host_in_access_list2)

    def read_history_lp(self):
        pass

    def view_packet_delay_graph(self):
        pass
# _________third_window____________________________

    def update_date_in_tables_on_third_window(self):
        self.ui.t_all_hosts.clear()
        self.ui.t_all_hosts.setRowCount(len(self.current_hosts))

        self.ui.t_all_hosts.setHorizontalHeaderLabels(
            ['id', 'Имя хоста', 'IP-адрес хоста', 'Аварийный сигнал', 'Описание'])
        for i, string in enumerate(self.current_hosts):
            self.ui.t_all_hosts.setItem(i, 0,
                                        self.set_item_in_table(string,
                                                               'id'))
            self.ui.t_all_hosts.setItem(i, 1,
                                        self.set_item_in_table(string,
                                                               'name'))
            self.ui.t_all_hosts.setItem(i, 2,
                                        self.set_item_in_table(string,
                                                               'ip_add'))
            self.ui.t_all_hosts.setItem(i, 3,
                                        self.set_item_in_table(string,
                                                               'alarm')
                                        )
            self.ui.t_all_hosts.setItem(i, 4,
                                        self.set_item_in_table(string,
                                                               'descr')
                                        )

        self.ui.t_all_hosts.setSizePolicy(QSizePolicy.Expanding,
                                          QSizePolicy.Expanding)

        (self.ui.t_all_hosts.horizontalHeader().
         setSectionResizeMode(QHeaderView.ResizeToContents))

        (self.ui.t_all_hosts.verticalHeader().
         setSectionResizeMode(QHeaderView.ResizeToContents))

        self.ui.t_all_hosts.horizontalHeader().setStretchLastSection(True)
        self.ui.t_all_hosts.setSortingEnabled(True)

    @staticmethod
    def set_item_in_table(host, host_atr):
        item = QTableWidgetItem()
        item.setForeground(QBrush(QColor('blue')))
        item.setData(Qt.EditRole, getattr(host, host_atr))
        return item

    def parse_third_window(self, char):
        self.ui.t_all_hosts.clear()
        data = []
        for item in self.hosts_iter_third_window:
            if char.lower() in item.lower():
                data.append(int(self.get_id_host(item)))
        data_with_hosts = []
        for host in self.all_hosts:
            if host.id in data:
                data_with_hosts.append(host)
        self.current_hosts = data_with_hosts
        self.update_date_in_tables_on_third_window()

    def handle_cell_clicked(self, row, column):
        item = self.ui.t_all_hosts.item(row, 0)
        if item is not None:
            self.id_host_in_table = int(item.text())
            self.ui.b_del.setDisabled(False)
            self.ui.b_edit.setDisabled(False)

    def update_buttons_on_third_window(self):
        self.ui.b_del.setDisabled(True)
        self.ui.b_edit.setDisabled(True)

    def add_host(self):
        self.window_add_and_edit.setWindowModality(Qt.ApplicationModal)
        self.window_add_and_edit.setWindowTitle('Окно добавления узла')
        self.window_add_and_edit.setStyleSheet(self.main_window.style_sheet)
        self.window_add_and_edit.init_add_host()
        self.window_add_and_edit.exec()

    def del_host(self):
        if str(self.id_host_in_table) in self.list_with_id_hosts:
            self.list_with_id_hosts.remove(str(self.id_host_in_table))
            self.save_changes()
        host = self.main_window.manager.wwh.read_info_about_host(
            self.id_host_in_table)
        self.main_window.manager.wwh.delete_host(self.id_host_in_table)
        try:
            self.window_add_and_edit.hosts_ip_add.remove(host.ip_add)
            self.window_add_and_edit.hosts_name.remove(host.name)
        except Exception as e:
            print(e)
        self.clear_setting_data()
        self.set_data()
        self.all_update()

    def edit_host(self):
        self.window_add_and_edit.setWindowModality(Qt.ApplicationModal)
        self.window_add_and_edit.setWindowTitle('Окно редактирования узла')
        self.window_add_and_edit.setStyleSheet(self.main_window.style_sheet)
        self.window_add_and_edit.init_edit_host(self.id_host_in_table)
        self.window_add_and_edit.exec()
