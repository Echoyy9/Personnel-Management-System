# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profess.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_profess(object):
    def setupUi(self, profess):
        profess.setObjectName("profess")
        profess.resize(917, 571)
        profess.setStyleSheet("background-color:#f4f9f4;")
        self.tableWidget = QtWidgets.QTableWidget(profess)
        self.tableWidget.setGeometry(QtCore.QRect(140, 120, 611, 351))
        self.tableWidget.setStyleSheet("border:outset;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(305)
        self.tableWidget.verticalHeader().setVisible(False)
        self.lineEdit = QtWidgets.QLineEdit(profess)
        self.lineEdit.setGeometry(QtCore.QRect(390, 40, 121, 21))
        self.lineEdit.setStyleSheet("font: 14pt \"华文行楷\";\n"
"color:rgb(80, 126, 59);\n"
"background-color:transparent;\n"
"border:outset;")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(profess)
        QtCore.QMetaObject.connectSlotsByName(profess)

    def retranslateUi(self, profess):
        _translate = QtCore.QCoreApplication.translate
        profess.setWindowTitle(_translate("profess", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("profess", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("profess", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("profess", "2"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("profess", "职位编号"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("profess", "职位名称"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setText(_translate("profess", "职位信息"))

