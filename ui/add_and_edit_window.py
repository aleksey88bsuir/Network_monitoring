# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_and_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(455, 424)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(455, 424))
        Dialog.setMaximumSize(QtCore.QSize(455, 424))
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 159, 141, 17))
        self.label_8.setObjectName("label_8")
        self.name_edit = QtWidgets.QLineEdit(Dialog)
        self.name_edit.setGeometry(QtCore.QRect(160, 85, 291, 31))
        self.name_edit.setObjectName("name_edit")
        self.l_warning_ip_add = QtWidgets.QLabel(Dialog)
        self.l_warning_ip_add.setGeometry(QtCore.QRect(160, 68, 291, 17))
        self.l_warning_ip_add.setText("")
        self.l_warning_ip_add.setObjectName("l_warning_ip_add")
        self.l_warning_name = QtWidgets.QLabel(Dialog)
        self.l_warning_name.setGeometry(QtCore.QRect(160, 121, 291, 17))
        self.l_warning_name.setObjectName("l_warning_name")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 91, 72, 17))
        self.label_3.setObjectName("label_3")
        self.ip_add_edit = QtWidgets.QLineEdit(Dialog)
        self.ip_add_edit.setGeometry(QtCore.QRect(160, 15, 291, 31))
        self.ip_add_edit.setObjectName("ip_add_edit")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(160, 45, 141, 23))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 17))
        self.label.setObjectName("label")
        self.alarm_edit = QtWidgets.QLineEdit(Dialog)
        self.alarm_edit.setGeometry(QtCore.QRect(160, 153, 251, 31))
        self.alarm_edit.setObjectName("alarm_edit")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 190, 101, 17))
        self.label_9.setObjectName("label_9")
        self.descr_edit = QtWidgets.QTextEdit(Dialog)
        self.descr_edit.setGeometry(QtCore.QRect(160, 190, 291, 192))
        self.descr_edit.setObjectName("descr_edit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 390, 251, 17))
        self.label_2.setObjectName("label_2")
        self.b_cancel = QtWidgets.QPushButton(Dialog)
        self.b_cancel.setGeometry(QtCore.QRect(270, 390, 89, 25))
        self.b_cancel.setObjectName("b_cancel")
        self.b_ok = QtWidgets.QPushButton(Dialog)
        self.b_ok.setGeometry(QtCore.QRect(362, 390, 89, 25))
        self.b_ok.setObjectName("b_ok")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 153, 31, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "Аварийный сигнал*"))
        self.l_warning_name.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "Имя хоста"))
        self.checkBox.setText(_translate("Dialog", "доменное имя"))
        self.label.setText(_translate("Dialog", "IP-адрес хоста"))
        self.label_9.setText(_translate("Dialog", "Описание*"))
        self.label_2.setText(_translate("Dialog", "* Не обязательно для заполнения"))
        self.b_cancel.setText(_translate("Dialog", "Отмена"))
        self.b_ok.setText(_translate("Dialog", "ОК"))
        self.pushButton.setText(_translate("Dialog", "..."))
