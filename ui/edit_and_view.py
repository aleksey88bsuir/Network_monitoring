from PyQt5 import QtWidgets
from ui.edit_and_view_window import Ui_Dialog


class EditAndViewWindow(QtWidgets.QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.set_data()
        self.start_interface()

    def start_interface(self):
        pass

    def set_data(self):
        pass
