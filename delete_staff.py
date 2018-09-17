# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_staff.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_delete_staff(object):
    def setupUi(self, delete_staff):
        delete_staff.setObjectName("delete_staff")
        delete_staff.resize(918, 571)
        delete_staff.setStyleSheet("background-color:#f4f9f4;")
        self.lineEdit = QtWidgets.QLineEdit(delete_staff)
        self.lineEdit.setGeometry(QtCore.QRect(390, 40, 121, 21))
        self.lineEdit.setStyleSheet("font: 14pt \"华文行楷\";\n"
"color:rgb(80, 126, 59);\n"
"background-color:transparent;\n"
"border:outset;")
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(delete_staff)
        self.tableWidget.setGeometry(QtCore.QRect(150, 100, 621, 351))
        self.tableWidget.setStyleSheet("border:outset;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
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
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.tableWidget.verticalHeader().setVisible(False)

        self.retranslateUi(delete_staff)
        QtCore.QMetaObject.connectSlotsByName(delete_staff)

    def retranslateUi(self, delete_staff):
        _translate = QtCore.QCoreApplication.translate
        delete_staff.setWindowTitle(_translate("delete_staff", "Form"))
        self.lineEdit.setText(_translate("delete_staff", "删除员工信息"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("delete_staff", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("delete_staff", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("delete_staff", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("delete_staff", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("delete_staff", "4"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("delete_staff", "工号"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("delete_staff", "姓名"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("delete_staff", "部门"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("delete_staff", "删除"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

