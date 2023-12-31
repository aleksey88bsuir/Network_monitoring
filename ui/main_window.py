# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.b_start = QtWidgets.QPushButton(self.centralwidget)
        self.b_start.setObjectName("b_start")
        self.verticalLayout.addWidget(self.b_start)
        self.b_stop = QtWidgets.QPushButton(self.centralwidget)
        self.b_stop.setObjectName("b_stop")
        self.verticalLayout.addWidget(self.b_stop)
        self.b_modify = QtWidgets.QPushButton(self.centralwidget)
        self.b_modify.setObjectName("b_modify")
        self.verticalLayout.addWidget(self.b_modify)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.q_volume_cont = QtWidgets.QDial(self.centralwidget)
        self.q_volume_cont.setObjectName("q_volume_cont")
        self.verticalLayout_2.addWidget(self.q_volume_cont)
        self.l_volume = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_volume.sizePolicy().hasHeightForWidth())
        self.l_volume.setSizePolicy(sizePolicy)
        self.l_volume.setText("")
        self.l_volume.setAlignment(QtCore.Qt.AlignCenter)
        self.l_volume.setObjectName("l_volume")
        self.verticalLayout_2.addWidget(self.l_volume)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.cb_mode_work = QtWidgets.QComboBox(self.centralwidget)
        self.cb_mode_work.setObjectName("cb_mode_work")
        self.cb_mode_work.addItem("")
        self.cb_mode_work.addItem("")
        self.verticalLayout_4.addWidget(self.cb_mode_work)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.cd_style = QtWidgets.QComboBox(self.centralwidget)
        self.cd_style.setObjectName("cd_style")
        self.verticalLayout_4.addWidget(self.cd_style)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.verticalLayout_5.addWidget(self.picture)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(620, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_6.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.about_program = QtWidgets.QAction(MainWindow)
        self.about_program.setObjectName("about_program")
        self.about_author = QtWidgets.QAction(MainWindow)
        self.about_author.setObjectName("about_author")
        self.tutorial = QtWidgets.QAction(MainWindow)
        self.tutorial.setObjectName("tutorial")
        self.read_log = QtWidgets.QAction(MainWindow)
        self.read_log.setObjectName("read_log")
        self.clear_log = QtWidgets.QAction(MainWindow)
        self.clear_log.setObjectName("clear_log")
        self.menu.addAction(self.read_log)
        self.menu.addAction(self.clear_log)
        self.menu_2.addAction(self.about_program)
        self.menu_2.addAction(self.about_author)
        self.menu_2.addAction(self.tutorial)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_start.setText(_translate("MainWindow", "Запуск\n"
"мониторинга"))
        self.b_stop.setText(_translate("MainWindow", "Остановка\n"
"мониторинга"))
        self.b_modify.setText(_translate("MainWindow", "Изменить таблицу/\n"
"просмотреть данные"))
        self.label.setText(_translate("MainWindow", "Режим работы"))
        self.cb_mode_work.setItemText(0, _translate("MainWindow", "Многопоточный"))
        self.cb_mode_work.setItemText(1, _translate("MainWindow", "Асинхронный"))
        self.label_2.setText(_translate("MainWindow", "Внешний вид"))
        self.label_3.setText(_translate("MainWindow", "Здесь может быть размещена \n"
"Ваша реклама"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя хоста"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP адрес хоста"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Статус в сети"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Время задержки"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Информация"))
        self.about_program.setText(_translate("MainWindow", "О программе"))
        self.about_author.setText(_translate("MainWindow", "Об авторе"))
        self.tutorial.setText(_translate("MainWindow", "Руководство по эксплуатации"))
        self.read_log.setText(_translate("MainWindow", "Просмотреть log файл"))
        self.clear_log.setText(_translate("MainWindow", "Очистить log файл"))
