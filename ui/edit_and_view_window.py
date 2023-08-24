# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_and_view_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 590)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l_search_string = QtWidgets.QLabel(self.widget)
        self.l_search_string.setObjectName("l_search_string")
        self.gridLayout_2.addWidget(self.l_search_string, 0, 0, 1, 1)
        self.search_line = QtWidgets.QLineEdit(self.widget)
        self.search_line.setObjectName("search_line")
        self.gridLayout_2.addWidget(self.search_line, 1, 0, 1, 1)
        self.l_list_with_access_hosts = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_list_with_access_hosts.sizePolicy().hasHeightForWidth())
        self.l_list_with_access_hosts.setSizePolicy(sizePolicy)
        self.l_list_with_access_hosts.setObjectName("l_list_with_access_hosts")
        self.gridLayout_2.addWidget(self.l_list_with_access_hosts, 2, 0, 1, 1)
        self.list_access_hosts = QtWidgets.QListWidget(self.widget)
        self.list_access_hosts.setObjectName("list_access_hosts")
        self.gridLayout_2.addWidget(self.list_access_hosts, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b_up = QtWidgets.QPushButton(self.widget)
        self.b_up.setObjectName("b_up")
        self.horizontalLayout.addWidget(self.b_up)
        self.b_save_changes = QtWidgets.QPushButton(self.widget)
        self.b_save_changes.setObjectName("b_save_changes")
        self.horizontalLayout.addWidget(self.b_save_changes)
        self.b_down = QtWidgets.QPushButton(self.widget)
        self.b_down.setObjectName("b_down")
        self.horizontalLayout.addWidget(self.b_down)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.l_list_of_hosts_to_work_with = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_list_of_hosts_to_work_with.sizePolicy().hasHeightForWidth())
        self.l_list_of_hosts_to_work_with.setSizePolicy(sizePolicy)
        self.l_list_of_hosts_to_work_with.setObjectName("l_list_of_hosts_to_work_with")
        self.gridLayout_2.addWidget(self.l_list_of_hosts_to_work_with, 5, 0, 1, 1)
        self.list_working_hosts = QtWidgets.QListWidget(self.widget)
        self.list_working_hosts.setObjectName("list_working_hosts")
        self.gridLayout_2.addWidget(self.list_working_hosts, 6, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.list_with_access_hosts2 = QtWidgets.QListWidget(self.tab_2)
        self.list_with_access_hosts2.setObjectName("list_with_access_hosts2")
        self.gridLayout.addWidget(self.list_with_access_hosts2, 3, 0, 1, 1)
        self.l_access_line = QtWidgets.QLabel(self.tab_2)
        self.l_access_line.setObjectName("l_access_line")
        self.gridLayout.addWidget(self.l_access_line, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_with = QtWidgets.QLabel(self.tab_2)
        self.l_with.setObjectName("l_with")
        self.verticalLayout.addWidget(self.l_with)
        self.start_date_and_time = QtWidgets.QDateTimeEdit(self.tab_2)
        self.start_date_and_time.setObjectName("start_date_and_time")
        self.verticalLayout.addWidget(self.start_date_and_time)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.l_finish = QtWidgets.QLabel(self.tab_2)
        self.l_finish.setObjectName("l_finish")
        self.verticalLayout_4.addWidget(self.l_finish)
        self.finish_date_and_time = QtWidgets.QDateTimeEdit(self.tab_2)
        self.finish_date_and_time.setObjectName("finish_date_and_time")
        self.verticalLayout_4.addWidget(self.finish_date_and_time)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.time_filter = QtWidgets.QCheckBox(self.tab_2)
        self.time_filter.setObjectName("time_filter")
        self.gridLayout.addWidget(self.time_filter, 5, 0, 1, 1)
        self.l_search_line = QtWidgets.QLabel(self.tab_2)
        self.l_search_line.setObjectName("l_search_line")
        self.gridLayout.addWidget(self.l_search_line, 0, 0, 1, 1)
        self.search_edit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.search_edit_2.setObjectName("search_edit_2")
        self.gridLayout.addWidget(self.search_edit_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.b_read_history_connection = QtWidgets.QPushButton(self.tab_2)
        self.b_read_history_connection.setObjectName("b_read_history_connection")
        self.horizontalLayout_4.addWidget(self.b_read_history_connection)
        self.b_read_history_lp = QtWidgets.QPushButton(self.tab_2)
        self.b_read_history_lp.setObjectName("b_read_history_lp")
        self.horizontalLayout_4.addWidget(self.b_read_history_lp)
        self.b_view_packet_delay_graph = QtWidgets.QPushButton(self.tab_2)
        self.b_view_packet_delay_graph.setObjectName("b_view_packet_delay_graph")
        self.horizontalLayout_4.addWidget(self.b_view_packet_delay_graph)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.search_line_2 = QtWidgets.QLineEdit(self.tab)
        self.search_line_2.setObjectName("search_line_2")
        self.verticalLayout_3.addWidget(self.search_line_2)
        self.t_all_hosts = QtWidgets.QTableWidget(self.tab)
        self.t_all_hosts.setObjectName("t_all_hosts")
        self.t_all_hosts.setColumnCount(5)
        self.t_all_hosts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.t_all_hosts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.t_all_hosts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.t_all_hosts.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.t_all_hosts.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.t_all_hosts.setHorizontalHeaderItem(4, item)
        self.verticalLayout_3.addWidget(self.t_all_hosts)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_add = QtWidgets.QPushButton(self.tab)
        self.b_add.setObjectName("b_add")
        self.horizontalLayout_2.addWidget(self.b_add)
        self.b_del = QtWidgets.QPushButton(self.tab)
        self.b_del.setObjectName("b_del")
        self.horizontalLayout_2.addWidget(self.b_del)
        self.b_edit = QtWidgets.QPushButton(self.tab)
        self.b_edit.setObjectName("b_edit")
        self.horizontalLayout_2.addWidget(self.b_edit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_7.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.l_search_string.setText(_translate("Dialog", "Строка поиска"))
        self.l_list_with_access_hosts.setText(_translate("Dialog", "Список всех доступных узлов (хостов)"))
        self.b_up.setText(_translate("Dialog", "Вверх"))
        self.b_save_changes.setText(_translate("Dialog", "Сохранить изменения"))
        self.b_down.setText(_translate("Dialog", "Вниз"))
        self.l_list_of_hosts_to_work_with.setText(_translate("Dialog", "Список текущих узлов (хостов)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Dialog", "Tab 1"))
        self.l_access_line.setText(_translate("Dialog", "Список всех доступных узлов (хостов)"))
        self.l_with.setText(_translate("Dialog", "С"))
        self.l_finish.setText(_translate("Dialog", "По"))
        self.time_filter.setText(_translate("Dialog", "Включить фильтр времени"))
        self.l_search_line.setText(_translate("Dialog", "Строка поиска"))
        self.b_read_history_connection.setText(_translate("Dialog", "Посмотреть историю \n"
" подключений"))
        self.b_read_history_lp.setText(_translate("Dialog", "Посмотреть историю \n"
" потеряных пакетов"))
        self.b_view_packet_delay_graph.setText(_translate("Dialog", "Посмотреть график \n"
" задержки сигнала"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "nnnnn"))
        self.label.setText(_translate("Dialog", "Строка поиска"))
        item = self.t_all_hosts.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "id"))
        item = self.t_all_hosts.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Имя хоста"))
        item = self.t_all_hosts.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "IP-адрес хоста"))
        item = self.t_all_hosts.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Аварийный сигнал"))
        item = self.t_all_hosts.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Описание"))
        self.b_add.setText(_translate("Dialog", "Добавить"))
        self.b_del.setText(_translate("Dialog", "Удалить"))
        self.b_edit.setText(_translate("Dialog", "Редактировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Страница"))
