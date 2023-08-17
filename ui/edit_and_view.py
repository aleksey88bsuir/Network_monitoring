from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from ui.edit_and_view_window import Ui_Dialog
from manager import Manager
from search_host import HostsIter


class EditAndViewWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.access_hosts = None
        self.working_hosts = None
        self.hosts_iter = HostsIter()
        self.manager = Manager()
        self.init()

    def init(self):
        self.start_interface()
        self.set_data()

    def start_interface(self):
        self.ui.tabWidget.setTabText(0, "Редактировать таблицу")
        self.ui.tabWidget.setTabText(1, "Просмотр сведений")
        self.ui.search_line.textChanged.connect(self.parse)
        self.ui.search_edit.textChanged.connect(self.parse)

    def set_data(self):
        self.access_hosts = self.manager.read_all_hosts()
        self.working_hosts = self.manager.read_hosts_status()
        for host in self.access_hosts.values():
            self.hosts_iter.add_new_host(str(host))
            self.ui.list_access_hosts.addItem(QListWidgetItem(str(host)))

    def parse(self, char):
        self.ui.list_access_hosts.clear()
        data = []
        for item in self.hosts_iter:
            if char.lower() in item.lower():
                data.append(item)
        for string_item in data:
            item_ = QListWidgetItem(string_item)
            self.ui.list_access_hosts.addItem(item_)
