# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_profess.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_profess(object):
    def setupUi(self, add_profess):
        add_profess.setObjectName("add_profess")
        add_profess.resize(299, 230)
        add_profess.setStyleSheet("background-color:#f4f9f4;")
        self.pname = QtWidgets.QLineEdit(add_profess)
        self.pname.setGeometry(QtCore.QRect(90, 70, 121, 31))
        self.pname.setObjectName("pname")
        self.pushButton = QtWidgets.QPushButton(add_profess)
        self.pushButton.setGeometry(QtCore.QRect(110, 140, 75, 23))
        self.pushButton.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:3px;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(add_profess)
        self.pushButton.clicked.connect(add_profess.add)
        QtCore.QMetaObject.connectSlotsByName(add_profess)

    def retranslateUi(self, add_profess):
        _translate = QtCore.QCoreApplication.translate
        add_profess.setWindowTitle(_translate("add_profess", "添加职位名称"))
        self.pname.setPlaceholderText(_translate("add_profess", "请输入职位名称"))
        self.pushButton.setText(_translate("add_profess", "添加"))

