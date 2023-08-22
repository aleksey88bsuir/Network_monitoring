from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from ui.edit_and_view_window import Ui_Dialog
from search_host import HostsIter
from list_of_hosts_we_work_with import write_current_hosts


class EditAndViewWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.access_hosts = None
        self.working_hosts = None
        self.list_with_id_hosts = []
        self.hosts_iter = HostsIter()

    def init(self):
        self.start_interface()
        self.set_data()
        self.update_date_in_tables()
        self.update_buttons()

    def start_interface(self):
        self.ui.tabWidget.setTabText(0, "Выбор хостов для работы")
        self.ui.tabWidget.setTabText(1, "Информация о хостах")
        self.ui.tabWidget.setTabText(2, "Редактор таблицы")
        self.ui.search_line.textChanged.connect(self.parse)
        self.ui.search_edit.textChanged.connect(self.parse)
        self.ui.list_access_hosts.itemSelectionChanged.connect(
            self.handle_selection_change_access_list)
        self.ui.list_working_hosts.itemSelectionChanged.connect(
            self.handle_selection_change_work_list)
        self.ui.b_up.clicked.connect(self.move_up)
        self.ui.b_down.clicked.connect(self.move_down)
        self.ui.b_save_changes.clicked.connect(self.save_changes)
        self.ui.b_save_changes.setDisabled(True)
        self.update_buttons()

    def set_data(self):
        self.access_hosts = \
            [str(host) for host
             in self.main_window.manager.read_all_hosts().values()]

        self.working_hosts = \
            [str(host) for host
             in self.main_window.manager.read_hosts_status()]

        for host in self.working_hosts:
            self.list_with_id_hosts.append(self.get_id_host(host))

    def update_date_in_tables(self):
        self.ui.list_access_hosts.clear()
        self.ui.list_working_hosts.clear()
        for host in self.access_hosts:
            self.hosts_iter.add_new_host(str(host))
            self.ui.list_access_hosts.addItem(QListWidgetItem(str(host)))
        for host in self.working_hosts:
            self.ui.list_working_hosts.addItem(QListWidgetItem(str(host)))

    def parse(self, char):
        self.ui.list_access_hosts.clear()
        data = []
        for item in self.hosts_iter:
            if char.lower() in item.lower():
                data.append(item)
        for string_item in data:
            item_ = QListWidgetItem(string_item)
            self.ui.list_access_hosts.addItem(item_)

    def handle_selection_change_access_list(self):
        self.update_buttons()
        self.ui.b_down.setDisabled(False)

    def handle_selection_change_work_list(self):
        self.update_buttons()
        self.ui.b_up.setDisabled(False)

    def update_buttons(self):
        self.ui.b_down.setDisabled(True)
        self.ui.b_up.setDisabled(True)

    def move_up(self):
        selected_item = self.ui.list_working_hosts.currentItem()
        host_id = self.get_id_host(selected_item.text())
        self.list_with_id_hosts.remove(host_id)
        self.working_hosts.remove(selected_item.text())
        self.update_date_in_tables()
        self.update_buttons()
        self.ui.b_save_changes.setDisabled(False)

    def add_host(self):
        pass

    def save_changes(self):
        write_current_hosts(self.list_with_id_hosts)
        self.ui.b_save_changes.setDisabled(True)
        self.main_window.manager.dict_of_hosts_we_work_with()
        self.main_window.refresh_table()

    def del_host(self):
        selected_item = self.ui.list_working_hosts.currentItem()
        host_id = self.get_id_host(selected_item.text())
        self.access_hosts.remove(host_id)
        if host_id in self.list_with_id_hosts:
            self.list_with_id_hosts.remove(host_id)
            self.working_hosts.remove(host_id)
        # self.main_window.wwh.delete_host(host_id)
        self.update_buttons()
        self.update_date_in_tables()

    def edit_host(self):
        selected_item = self.ui.list_working_hosts.currentItem()
        host_id = self.get_id_host(selected_item.text())

    def move_down(self):
        selected_item = self.ui.list_access_hosts.currentItem()
        host_id = self.get_id_host(selected_item.text())
        if host_id not in self.list_with_id_hosts:
            self.list_with_id_hosts.append(host_id)
            self.working_hosts.append(selected_item.text())
            self.update_date_in_tables()
            self.update_buttons()
            self.ui.b_save_changes.setDisabled(False)

    @staticmethod
    def get_id_host(info_string):
        import re
        ip_add_pattern = r'(\d+) --'
        host_id_ = re.findall(ip_add_pattern, info_string)[0]
        return host_id_
