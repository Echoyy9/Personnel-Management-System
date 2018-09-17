# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_admin(object):
    def setupUi(self, add_admin):
        add_admin.setObjectName("add_admin")
        add_admin.resize(299, 230)
        add_admin.setStyleSheet("background-color:#f4f9f4;")
        self.pwd = QtWidgets.QLineEdit(add_admin)
        self.pwd.setGeometry(QtCore.QRect(110, 100, 121, 31))
        self.pwd.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pwd.setPlaceholderText("")
        self.pwd.setObjectName("pwd")
        self.pushButton = QtWidgets.QPushButton(add_admin)
        self.pushButton.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.pushButton.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:3px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(add_admin)
        self.label.setGeometry(QtCore.QRect(30, 40, 71, 21))
        self.label.setStyleSheet("font: 11pt \"华文细黑\";")
        self.label.setObjectName("label")
        self.staff = QtWidgets.QComboBox(add_admin)
        self.staff.setGeometry(QtCore.QRect(110, 40, 121, 31))
        self.staff.setObjectName("staff")
        self.label_2 = QtWidgets.QLabel(add_admin)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 71, 21))
        self.label_2.setStyleSheet("font: 11pt \"华文细黑\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(add_admin)
        self.pushButton.clicked.connect(add_admin.add)
        QtCore.QMetaObject.connectSlotsByName(add_admin)

    def retranslateUi(self, add_admin):
        _translate = QtCore.QCoreApplication.translate
        add_admin.setWindowTitle(_translate("add_admin", "添加管理员"))
        self.pushButton.setText(_translate("add_admin", "添加"))
        self.label.setText(_translate("add_admin", "选择员工:"))
        self.label_2.setText(_translate("add_admin", "设置密码:"))

