# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_dept.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_dept(object):
    def setupUi(self, add_dept):
        add_dept.setObjectName("add_dept")
        add_dept.resize(917, 571)
        add_dept.setStyleSheet("background-color:#f4f9f4;")
        self.name = QtWidgets.QLineEdit(add_dept)
        self.name.setGeometry(QtCore.QRect(440, 140, 121, 31))
        self.name.setObjectName("name")
        self.label1 = QtWidgets.QLabel(add_dept)
        self.label1.setGeometry(QtCore.QRect(340, 140, 81, 31))
        self.label1.setStyleSheet("font: 12pt \"幼圆\";")
        self.label1.setObjectName("label1")
        self.pushButton_2 = QtWidgets.QPushButton(add_dept)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 330, 75, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:3px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(add_dept)
        self.pushButton.setGeometry(QtCore.QRect(480, 330, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:3px;")
        self.pushButton.setObjectName("pushButton")
        self.label2 = QtWidgets.QLabel(add_dept)
        self.label2.setGeometry(QtCore.QRect(340, 220, 81, 31))
        self.label2.setStyleSheet("font: 12pt \"幼圆\";")
        self.label2.setObjectName("label2")
        self.lineEdit = QtWidgets.QLineEdit(add_dept)
        self.lineEdit.setGeometry(QtCore.QRect(390, 40, 121, 21))
        self.lineEdit.setStyleSheet("font: 14pt \"华文行楷\";\n"
"color:rgb(80, 126, 59);\n"
"background-color:transparent;\n"
"border:outset;")
        self.lineEdit.setObjectName("lineEdit")
        self.manager = QtWidgets.QComboBox(add_dept)
        self.manager.setGeometry(QtCore.QRect(440, 220, 121, 31))
        self.manager.setObjectName("manager")
        self.label1.setBuddy(self.name)

        self.retranslateUi(add_dept)
        self.pushButton_2.clicked.connect(add_dept.addDept)
        self.pushButton.clicked.connect(add_dept.clearAll)
        QtCore.QMetaObject.connectSlotsByName(add_dept)

    def retranslateUi(self, add_dept):
        _translate = QtCore.QCoreApplication.translate
        add_dept.setWindowTitle(_translate("add_dept", "Form"))
        self.name.setPlaceholderText(_translate("add_dept", "不超过10个中文字符"))
        self.label1.setText(_translate("add_dept", "部门名称："))
        self.pushButton_2.setText(_translate("add_dept", "添加"))
        self.pushButton.setText(_translate("add_dept", "清空"))
        self.label2.setText(_translate("add_dept", "部门经理："))
        self.lineEdit.setText(_translate("add_dept", "增加部门信息"))

