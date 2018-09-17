# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find_staff.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_find_staff(object):
    def setupUi(self, find_staff):
        find_staff.setObjectName("find_staff")
        find_staff.resize(917, 571)
        find_staff.setStyleSheet("background-color:#f4f9f4;")
        self.lineEdit = QtWidgets.QLineEdit(find_staff)
        self.lineEdit.setGeometry(QtCore.QRect(390, 40, 121, 21))
        self.lineEdit.setStyleSheet("font: 14pt \"华文行楷\";\n"
"color:rgb(80, 126, 59);\n"
"background-color:transparent;\n"
"border:outset;")
        self.lineEdit.setObjectName("lineEdit")
        self.searchBox = QtWidgets.QLineEdit(find_staff)
        self.searchBox.setGeometry(QtCore.QRect(530, 110, 171, 31))
        self.searchBox.setStyleSheet("background:transparent;\n"
"border:1px solid black;\n"
"border-radius:10px;")
        self.searchBox.setObjectName("searchBox")
        self.tableWidget = QtWidgets.QTableWidget(find_staff)
        self.tableWidget.setGeometry(QtCore.QRect(140, 170, 611, 311))
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
        self.pushButton = QtWidgets.QPushButton(find_staff)
        self.pushButton.setGeometry(QtCore.QRect(710, 110, 31, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/images/search2.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(find_staff)
        self.pushButton.clicked.connect(find_staff.search)
        self.searchBox.textChanged['QString'].connect(find_staff.showall)
        QtCore.QMetaObject.connectSlotsByName(find_staff)

    def retranslateUi(self, find_staff):
        _translate = QtCore.QCoreApplication.translate
        find_staff.setWindowTitle(_translate("find_staff", "Form"))
        self.lineEdit.setText(_translate("find_staff", "查询员工信息"))
        self.searchBox.setPlaceholderText(_translate("find_staff", "输入查找的工号"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("find_staff", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("find_staff", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("find_staff", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("find_staff", "3"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("find_staff", "工号"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("find_staff", "姓名"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("find_staff", "查看"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

import img_rc
