# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finde_dept.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_find_dept(object):
    def setupUi(self, find_dept):
        find_dept.setObjectName("find_dept")
        find_dept.resize(715, 646)
        find_dept.setStyleSheet("background-color:#f4f9f4;")
        self.pushButton = QtWidgets.QPushButton(find_dept)
        self.pushButton.setGeometry(QtCore.QRect(620, 100, 31, 31))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/images/search2.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(find_dept)
        self.tableWidget.setGeometry(QtCore.QRect(50, 160, 611, 201))
        self.tableWidget.setStyleSheet("border:outset;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(203)
        self.tableWidget.verticalHeader().setVisible(False)
        self.searchBox = QtWidgets.QLineEdit(find_dept)
        self.searchBox.setGeometry(QtCore.QRect(440, 100, 171, 31))
        self.searchBox.setStyleSheet("background:transparent;\n"
"border:1px solid black;\n"
"border-radius:10px;")
        self.searchBox.setObjectName("searchBox")
        self.lineEdit = QtWidgets.QLineEdit(find_dept)
        self.lineEdit.setGeometry(QtCore.QRect(300, 40, 121, 21))
        self.lineEdit.setStyleSheet("font: 14pt \"华文行楷\";\n"
"color:rgb(80, 126, 59);\n"
"background-color:transparent;\n"
"border:outset;")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(find_dept)
        self.pushButton.clicked.connect(find_dept.search)
        self.searchBox.textChanged['QString'].connect(find_dept.showall)
        QtCore.QMetaObject.connectSlotsByName(find_dept)

    def retranslateUi(self, find_dept):
        _translate = QtCore.QCoreApplication.translate
        find_dept.setWindowTitle(_translate("find_dept", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("find_dept", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("find_dept", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("find_dept", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("find_dept", "3"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("find_dept", "部门编号"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("find_dept", "部门名称"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("find_dept", "详细信息"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.searchBox.setPlaceholderText(_translate("find_dept", "输入查找的部门编号"))
        self.lineEdit.setText(_translate("find_dept", "查询部门信息"))

import img_rc
