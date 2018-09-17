# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alter_admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_alter_admin(object):
    def setupUi(self, alter_admin):
        alter_admin.setObjectName("alter_admin")
        alter_admin.resize(299, 230)
        alter_admin.setStyleSheet("background-color:#f4f9f4;")
        self.pwd = QtWidgets.QLineEdit(alter_admin)
        self.pwd.setGeometry(QtCore.QRect(80, 90, 141, 31))
        self.pwd.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pwd.setObjectName("pwd")
        self.pushButton = QtWidgets.QPushButton(alter_admin)
        self.pushButton.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.pushButton.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:3px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(alter_admin)
        self.label.setGeometry(QtCore.QRect(80, 50, 31, 21))
        self.label.setStyleSheet("color:rgb(124, 124, 124);")
        self.label.setObjectName("label")
        self.sno = QtWidgets.QLineEdit(alter_admin)
        self.sno.setGeometry(QtCore.QRect(120, 50, 51, 21))
        self.sno.setStyleSheet("border:outset;\n"
"color:rgb(124, 124, 124);")
        self.sno.setText("")
        self.sno.setObjectName("sno")

        self.retranslateUi(alter_admin)
        self.pushButton.clicked.connect(alter_admin.save)
        QtCore.QMetaObject.connectSlotsByName(alter_admin)

    def retranslateUi(self, alter_admin):
        _translate = QtCore.QCoreApplication.translate
        alter_admin.setWindowTitle(_translate("alter_admin", "修改密码"))
        self.pwd.setPlaceholderText(_translate("alter_admin", "输入新密码"))
        self.pushButton.setText(_translate("alter_admin", "保存"))
        self.label.setText(_translate("alter_admin", "工号："))

