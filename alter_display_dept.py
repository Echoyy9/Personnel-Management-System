# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alter_display_dept.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_alter_display_dept(object):
    def setupUi(self, alter_display_dept):
        alter_display_dept.setObjectName("alter_display_dept")
        alter_display_dept.resize(917, 571)
        alter_display_dept.setStyleSheet("background-color:#f4f9f4;")
        self.lineEdit = QtWidgets.QLineEdit(alter_display_dept)
        self.lineEdit.setGeometry(QtCore.QRect(390, 40, 121, 21))
        self.lineEdit.setStyleSheet("font: 14pt \"华文行楷\";\n"
"color:rgb(80, 126, 59);\n"
"background-color:transparent;\n"
"border:outset;")
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(alter_display_dept)
        self.tableWidget.setGeometry(QtCore.QRect(140, 100, 621, 421))
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

        self.retranslateUi(alter_display_dept)
        QtCore.QMetaObject.connectSlotsByName(alter_display_dept)

    def retranslateUi(self, alter_display_dept):
        _translate = QtCore.QCoreApplication.translate
        alter_display_dept.setWindowTitle(_translate("alter_display_dept", "Form"))
        self.lineEdit.setText(_translate("alter_display_dept", "修改部门信息"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("alter_display_dept", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("alter_display_dept", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("alter_display_dept", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("alter_display_dept", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("alter_display_dept", "4"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("alter_display_dept", "部门编号"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("alter_display_dept", "部门名称"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("alter_display_dept", "部门经理"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("alter_display_dept", "修改"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

