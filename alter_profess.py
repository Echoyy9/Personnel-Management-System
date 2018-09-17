# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alter_profess.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_alter_profess(object):
    def setupUi(self, alter_profess):
        alter_profess.setObjectName("alter_profess")
        alter_profess.resize(299, 230)
        alter_profess.setStyleSheet("background-color:#f4f9f4;")
        self.pname = QtWidgets.QLineEdit(alter_profess)
        self.pname.setGeometry(QtCore.QRect(90, 70, 121, 31))
        self.pname.setObjectName("pname")
        self.pushButton = QtWidgets.QPushButton(alter_profess)
        self.pushButton.setGeometry(QtCore.QRect(110, 140, 75, 23))
        self.pushButton.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:3px;")
        self.pushButton.setObjectName("pushButton")
        self.no = QtWidgets.QLineEdit(alter_profess)
        self.no.setGeometry(QtCore.QRect(150, 30, 61, 20))
        self.no.setStyleSheet("background:transparent;\n"
"border:outset;\n"
"color: rgb(138, 138, 138);")
        self.no.setObjectName("no")
        self.label = QtWidgets.QLabel(alter_profess)
        self.label.setGeometry(QtCore.QRect(90, 30, 54, 21))
        self.label.setStyleSheet("\n"
"color: rgb(138, 138, 138);")
        self.label.setObjectName("label")

        self.retranslateUi(alter_profess)
        self.pushButton.clicked.connect(alter_profess.save)
        QtCore.QMetaObject.connectSlotsByName(alter_profess)

    def retranslateUi(self, alter_profess):
        _translate = QtCore.QCoreApplication.translate
        alter_profess.setWindowTitle(_translate("alter_profess", "修改职位名称"))
        self.pname.setPlaceholderText(_translate("alter_profess", "请输入新的职位名称"))
        self.pushButton.setText(_translate("alter_profess", "保存"))
        self.no.setText(_translate("alter_profess", "1"))
        self.label.setText(_translate("alter_profess", "职位编号："))

