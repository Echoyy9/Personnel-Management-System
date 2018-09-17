# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkTable.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
#考勤历史查询

import sys
import pymysql
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class checkHistory(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, check):
        check.setObjectName("check")
        check.resize(1052, 624)
        self.verticalLayoutWidget = QtWidgets.QWidget(check)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 870, 525))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.checkLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.checkLayout.setContentsMargins(0, 0, 0, 0)
        self.checkLayout.setObjectName("checkLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.searchButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #self.searchButton.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_3.addWidget(self.searchButton, 0, 2, 1, 1)
        self.searchText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        #self.searchText.setStyleSheet("font: 16pt \"Adobe Arabic\";")
        self.searchText.setText("")
        self.searchText.setObjectName("searchText")
        self.gridLayout_3.addWidget(self.searchText, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        #self.comboBox.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setStyleSheet("font: 30pt \"Adobe Arabic\";")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 1, 1, 1)
        self.checkLayout.addLayout(self.gridLayout_3)
        self.checkTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.checkTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.checkTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.checkTable.setEnabled(True)
        self.checkTable.setTabletTracking(False)
        self.checkTable.setAcceptDrops(False)
        self.checkTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkTable.setStyleSheet("")
        self.checkTable.setAlternatingRowColors(True)
        self.checkTable.setShowGrid(True)
        self.checkTable.setWordWrap(False)
        self.checkTable.setCornerButtonEnabled(True)
        self.checkTable.setObjectName("checkTable")
        self.checkTable.setColumnCount(9)
        self.checkTable.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.checkTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.checkTable.setHorizontalHeaderItem(8, item)
        self.checkTable.horizontalHeader().setVisible(True)
        self.checkTable.horizontalHeader().setCascadingSectionResizes(False)
        self.checkTable.horizontalHeader().setHighlightSections(True)
        self.checkTable.horizontalHeader().setSortIndicatorShown(False)
        self.checkTable.horizontalHeader().setStretchLastSection(True)
        self.checkTable.verticalHeader().setVisible(False)
        self.checkTable.verticalHeader().setCascadingSectionResizes(False)
        self.checkTable.verticalHeader().setSortIndicatorShown(False)
        self.checkTable.verticalHeader().setStretchLastSection(False)
        self.checkLayout.addWidget(self.checkTable)

        self.retranslateUi(check)
        QtCore.QMetaObject.connectSlotsByName(check)

        self.readMysql()
        self.searchButton.clicked.connect(self.searchRecord)
        self.searchText.editingFinished.connect(self.searchRecord)

        # 右键删除
        self.checkTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.checkTable.customContextMenuRequested[QtCore.QPoint].connect(self.MenuShow)

    def retranslateUi(self, check):
        _translate = QtCore.QCoreApplication.translate
        check.setWindowTitle(_translate("check", "Form"))
        self.searchButton.setText(_translate("check", "查询"))
        self.comboBox.setItemText(0, _translate("check", "按姓名查找"))
        self.comboBox.setItemText(1, _translate("check", "按工号查找"))
        self.comboBox.setItemText(2, _translate("check", "按部门查找"))
        self.comboBox.setItemText(3, _translate("check", "按日期查找"))
        self.checkTable.setSortingEnabled(False)
        item = self.checkTable.verticalHeaderItem(0)
        item.setText(_translate("check", "New Row"))
        item = self.checkTable.verticalHeaderItem(1)
        item.setText(_translate("check", "New Row"))
        item = self.checkTable.verticalHeaderItem(2)
        item.setText(_translate("check", "New Row"))
        item = self.checkTable.verticalHeaderItem(3)
        item.setText(_translate("check", "New Row"))
        item = self.checkTable.horizontalHeaderItem(0)
        item.setText(_translate("check", "员工编号"))
        item = self.checkTable.horizontalHeaderItem(1)
        item.setText(_translate("check", "姓名"))
        item = self.checkTable.horizontalHeaderItem(2)
        item.setText(_translate("check", "性别"))
        item = self.checkTable.horizontalHeaderItem(3)
        item.setText(_translate("check", "部门"))
        item = self.checkTable.horizontalHeaderItem(4)
        item.setText(_translate("check", "职位"))
        item = self.checkTable.horizontalHeaderItem(5)
        item.setText(_translate("check", "日期"))
        item = self.checkTable.horizontalHeaderItem(6)
        item.setText(_translate("check", "加班日"))
        item = self.checkTable.horizontalHeaderItem(7)
        item.setText(_translate("check", "请假日"))
        item = self.checkTable.horizontalHeaderItem(8)
        item.setText(_translate("check", "旷工日"))

    def readMysql(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,c_date,c_odays,c_ldays,c_adays "+\
              "from checking as c,staff as s,sp,department,professional " + \
              " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no order by (c.s_no+0) desc"

        try:
           cur.execute(sql)
        except Exception as e:
            print(e)
        len = cur.fetchall().__len__()

        cur.execute(sql)
        self.checkTable.setRowCount(len)

        k = 0
        for i in cur:
            w = 0
            for j in i:
                newItem = QtWidgets.QTableWidgetItem(str(j))
                self.checkTable.setItem(k, w, newItem)
                w += 1
            k += 1

        cur.close()
        db.close()

    def searchRecord(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        if (self.searchText.text() == ""):
            sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,c_date,c_odays,c_ldays,c_adays from checking as c,staff as s,sp,department,professional " + \
                  " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no order by (c.s_no+0) desc"

            cur.execute(sql)
            len = cur.fetchall().__len__()

            cur.execute(sql)
            self.checkTable.setRowCount(len)

            k = 0
            for i in cur:
                w = 0
                for j in i:
                    newItem = QtWidgets.QTableWidgetItem(str(j))
                    self.checkTable.setItem(k, w, newItem)
                    w += 1
                k += 1
            return

        # 输入框内容

        temp = self.searchText.text()

        s = '%' + temp + '%'

        # 分类查询
        conditionChoice = self.comboBox.currentText()

        if (conditionChoice == "按姓名查找"):
            sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,c_date,c_odays,c_ldays,c_adays from checking as c,staff as s,sp,department,professional " + \
                  " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no"+\
                  " and s.s_name LIKE '%s' order by (c.s_no+0) desc" %(s)


        elif (conditionChoice == "按工号查找"):
            sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,c_date,c_odays,c_ldays,c_adays from checking as c,staff as s,sp,department,professional " + \
                  " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no" + \
                  " and s.s_no LIKE '%s' order by (c.s_no+0) desc" % (s)

        elif (conditionChoice == "按部门查找"):
            sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,c_date,c_odays,c_ldays,c_adays from checking as c,staff as s,sp,department,professional " + \
                  " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no" + \
                  " and department.d_name LIKE '%s' order by (c.s_no+0) desc" % (s)

        elif (conditionChoice == "按日期查找"):
            sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,c_date,c_odays,c_ldays,c_adays from checking as c,staff as s,sp,department,professional " + \
                  " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no" + \
                  " and c.c_date LIKE '%s' order by (c.s_no+0) desc" % (s)

        self.checkTable.clearContents()
        # 清空表格

        # 重新查找后生成表格
        cur.execute(sql)
        len = cur.fetchall().__len__()

        cur.execute(sql)
        self.checkTable.setRowCount(len)

        k = 0
        for i in cur:
            w = 0
            for j in i:
                newItem = QtWidgets.QTableWidgetItem(str(j))
                self.checkTable.setItem(k, w, newItem)
                w += 1
            k += 1

        cur.close()
        db.close()

    def MenuShow(self):
        try:

            rightMenu = QtWidgets.QMenu(self.checkTable)
            removeAction = QtWidgets.QAction(u"删除", self,
                                             triggered=self.deleteItem)  # triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
            rightMenu.addAction(removeAction)

            rightMenu.exec_(QtGui.QCursor.pos())

        except Exception as e:
            print(e)

    def deleteItem(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        row = self.checkTable.currentRow()
        s_no = self.checkTable.item(row, 0).text()
        c_date = self.checkTable.item(row, 5).text()

        reply = QtWidgets.QMessageBox.question(self, '提示框',
                                               "确定要删除这条数据吗?", QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            # print("yes")
            sql = "delete from checking where s_no = '%s' and c_date = '%s'" % (s_no,c_date)
            try:
                cur.execute(sql)
            except Exception as e:
                print(e)

            self.checkTable.removeRow(row)
            db.commit()

        cur.close()
        db.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainMindow = checkHistory()
    mainMindow.show()
    sys.exit(app.exec_())
