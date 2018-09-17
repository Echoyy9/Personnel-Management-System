# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alter_dept.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_alter_dept(object):
    def setupUi(self, alter_dept):
        alter_dept.setObjectName("alter_dept")
        alter_dept.setEnabled(True)
        alter_dept.resize(917, 571)
        alter_dept.setStyleSheet("background-color:#f4f9f4;")
        self.back = QtWidgets.QPushButton(alter_dept)
        self.back.setEnabled(True)
        self.back.setGeometry(QtCore.QRect(60, 30, 31, 31))
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.setStyleSheet("border-image: url(:/newPrefix/images/back.png);")
        self.back.setText("")
        self.back.setObjectName("back")
        self.label_9 = QtWidgets.QLabel(alter_dept)
        self.label_9.setGeometry(QtCore.QRect(350, 160, 81, 31))
        self.label_9.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(alter_dept)
        self.label_2.setGeometry(QtCore.QRect(350, 300, 71, 31))
        self.label_2.setStyleSheet("font: 12pt \"幼圆\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(alter_dept)
        self.lineEdit.setGeometry(QtCore.QRect(390, 40, 121, 21))
        self.lineEdit.setStyleSheet("font: 14pt \"华文行楷\";\n"
"color:rgb(80, 126, 59);\n"
"background-color:transparent;\n"
"border:outset;")
        self.lineEdit.setObjectName("lineEdit")
        self.name = QtWidgets.QLineEdit(alter_dept)
        self.name.setGeometry(QtCore.QRect(440, 220, 121, 31))
        self.name.setStyleSheet("")
        self.name.setText("")
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(alter_dept)
        self.label.setGeometry(QtCore.QRect(350, 220, 81, 31))
        self.label.setStyleSheet("font: 12pt \"幼圆\";")
        self.label.setObjectName("label")
        self.no = QtWidgets.QLineEdit(alter_dept)
        self.no.setEnabled(False)
        self.no.setGeometry(QtCore.QRect(440, 160, 101, 31))
        self.no.setStyleSheet("border:outset;")
        self.no.setText("")
        self.no.setObjectName("no")
        self.pushButton = QtWidgets.QPushButton(alter_dept)
        self.pushButton.setGeometry(QtCore.QRect(480, 390, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:3px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(alter_dept)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 390, 75, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font:75 10pt \"黑体\";\n"
"color:white;\n"
"background-color:rgb(85,170,127);\n"
"border-radius:3px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.manager = QtWidgets.QComboBox(alter_dept)
        self.manager.setGeometry(QtCore.QRect(440, 300, 121, 31))
        self.manager.setObjectName("manager")
        self.label_9.setBuddy(self.no)
        self.label.setBuddy(self.name)

        self.retranslateUi(alter_dept)
        self.back.clicked.connect(alter_dept.goback)
        self.pushButton_2.clicked.connect(alter_dept.saveInfo)
        self.pushButton.clicked.connect(alter_dept.restore)
        QtCore.QMetaObject.connectSlotsByName(alter_dept)

    def retranslateUi(self, alter_dept):
        _translate = QtCore.QCoreApplication.translate
        alter_dept.setWindowTitle(_translate("alter_dept", "Form"))
        self.label_9.setText(_translate("alter_dept", "部门编号："))
        self.label_2.setText(_translate("alter_dept", "部门经理："))
        self.lineEdit.setText(_translate("alter_dept", "修改部门信息"))
        self.name.setPlaceholderText(_translate("alter_dept", "不超过10个中文字符"))
        self.label.setText(_translate("alter_dept", "部门名称："))
        self.pushButton.setText(_translate("alter_dept", "恢复"))
        self.pushButton_2.setText(_translate("alter_dept", "保存"))

import img_rc
