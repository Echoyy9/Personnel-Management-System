# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personalTable1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

#人员调动历史界面


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from personaldialog import changePersonelDialog

class personnel_history(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, personal):

        personal.setObjectName("personal")
        personal.resize(910, 589)
        self.searchButton = QtWidgets.QPushButton(personal)
        self.searchButton.setGeometry(QtCore.QRect(640, 10, 91, 30))
        self.searchButton.setObjectName("searchButton")
        self.comboBox = QtWidgets.QComboBox(personal)
        self.comboBox.setGeometry(QtCore.QRect(750, 10, 121, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.personalTable = QtWidgets.QTableWidget(personal)
        self.personalTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.personalTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.personalTable.setGeometry(QtCore.QRect(5, 52, 870, 490))
        self.personalTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.personalTable.setAlternatingRowColors(True)
        self.personalTable.setShowGrid(True)
        self.personalTable.setWordWrap(False)
        self.personalTable.setCornerButtonEnabled(True)
        self.personalTable.setObjectName("personalTable")
        self.personalTable.setColumnCount(9)
        self.personalTable.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.personalTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.personalTable.setHorizontalHeaderItem(8, item)

        self.personalTable.horizontalHeader().setSortIndicatorShown(False)
        self.personalTable.horizontalHeader().setStretchLastSection(True)
        self.personalTable.verticalHeader().setVisible(False)
        self.personalTable.verticalHeader().setCascadingSectionResizes(False)
        self.personalTable.verticalHeader().setSortIndicatorShown(False)
        self.personalTable.verticalHeader().setStretchLastSection(False)
        self.searchText = QtWidgets.QLineEdit(personal)
        self.searchText.setGeometry(QtCore.QRect(5, 10, 600,30))
        self.searchText.setObjectName("searchText")

        self.retranslateUi(personal)
        self.readMysql()
        self.searchButton.clicked.connect(self.searchRecord)
        self.searchText.editingFinished.connect(self.searchRecord)
        self.personalTable.doubleClicked.connect(self.changePerson)

        #右键删除
        self.personalTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.personalTable.customContextMenuRequested[QtCore.QPoint].connect(self.MenuShow)
        #self.personalTable.itemClicked.connect(self.MenuShow)

        QtCore.QMetaObject.connectSlotsByName(personal)

    def retranslateUi(self, personal):
        _translate = QtCore.QCoreApplication.translate
        personal.setWindowTitle(_translate("personal", "Form"))
        self.searchButton.setText(_translate("personal", "查询"))
        self.comboBox.setItemText(0, _translate("personal", "按姓名查找"))
        self.comboBox.setItemText(1, _translate("personal", "按工号查找"))
        self.personalTable.setSortingEnabled(False)
        item = self.personalTable.verticalHeaderItem(1)
        item.setText(_translate("personal", "New Row"))
        item = self.personalTable.verticalHeaderItem(2)
        item.setText(_translate("personal", "New Row"))
        item = self.personalTable.horizontalHeaderItem(0)
        item.setText(_translate("personal", "编号"))
        item = self.personalTable.horizontalHeaderItem(1)
        item.setText(_translate("personal", "员工编号"))
        item = self.personalTable.horizontalHeaderItem(2)
        item.setText(_translate("personal", "姓名"))
        item = self.personalTable.horizontalHeaderItem(3)
        item.setText(_translate("personal", "性别"))
        item = self.personalTable.horizontalHeaderItem(4)
        item.setText(_translate("personal", "原部门"))
        item = self.personalTable.horizontalHeaderItem(5)
        item.setText(_translate("personal", "原职位"))
        item = self.personalTable.horizontalHeaderItem(6)
        item.setText(_translate("personal", "新部门"))
        item = self.personalTable.horizontalHeaderItem(7)
        item.setText(_translate("personal", "新职位"))
        item = self.personalTable.horizontalHeaderItem(8)
        item.setText(_translate("personal", "时间"))

        __sortingEnabled = self.personalTable.isSortingEnabled()
        self.personalTable.setSortingEnabled(False)

        self.personalTable.setSortingEnabled(__sortingEnabled)

    def readMysql(self):
        db =  pymysql.connect("localhost","root", "123456",db="personnel_man")
        cur = db.cursor()
        
        sql = "select p.p_no,p.s_no,staff.s_name,staff.s_sex ,p.predept,p.prepost,p.aftdept,p.aftpost,p.p_date from personnel as p,staff where p.s_no = staff.s_no  Order By p.p_date desc,(p.p_no+0) desc "
        cur.execute(sql)
        len = cur.fetchall().__len__()

        cur.execute(sql)
        self.personalTable.setRowCount(len)

        k=0
        for i in cur:
            w=0
            for j in i:
                newItem = QtWidgets.QTableWidgetItem(str(j))
                self.personalTable.setItem(k,w,newItem)
                w += 1
            k+=1

        cur.close()
        db.close()

    # 点击查询
    def searchRecord(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()
        
        if (self.searchText.text() == ""):
            sql = "select p.p_no, p.s_no,staff.s_name,staff.s_sex,p.predept,p.prepost,p.aftdept,p.aftpost,p.p_date from personnel as p,staff "+\
                  "where p.s_no = staff.s_no Order By p.p_date desc,(p.p_no+0) desc  "
            cur.execute(sql)
            len = cur.fetchall().__len__()

            cur.execute(sql)
            self.personalTable.setRowCount(len)

            k = 0
            for i in cur:
                w = 0
                for j in i:
                    newItem = QtWidgets.QTableWidgetItem(str(j))
                    self.personalTable.setItem(k, w, newItem)
                    w += 1
                k += 1
            return

        #输入框内容

        temp = self.searchText.text()

        s = '%'+temp+'%'

        # 分类查询
        conditionChoice = self.comboBox.currentText()

        if (conditionChoice == "按姓名查找"):
            sql = "select p.p_no,p.s_no,staff.s_name,staff.s_sex,p.predept,p.prepost,p.aftdept,p.aftpost,p.p_date from personnel as p,staff where p.s_no = staff.s_no and staff.s_name LIKE '%s' Order By p.p_date desc,(p.p_no+0) desc" % ( s)
        elif (conditionChoice == "按工号查找"):
            sql = "select p.p_no,p.s_no,staff.s_name,staff.s_sex,p.predept,p.prepost,p.aftdept,p.aftpost,p.p_date from personnel as p,staff where p.s_no = staff.s_no and staff.s_no LIKE '%s'  Order By p.p_date desc,(p.p_no+0) desc " % (s)



        self.personalTable.clearContents()
        #清空表格

        #重新查找后生成表格
        cur.execute(sql)
        len = cur.fetchall().__len__()

        cur.execute(sql)
        self.personalTable.setRowCount(len)

        k=0
        for i in cur:
            w=0
            for j in i:
                newItem = QtWidgets.QTableWidgetItem(str(j))
                self.personalTable.setItem(k,w,newItem)
                w += 1
            k+=1

        if (self.searchText.text() == ""):
            pass

        cur.close()
        db.close()

    def changePerson(self):
        _translate = QtCore.QCoreApplication.translate
        row = self.personalTable.currentRow()
        sno = self.personalTable.item(row,1).text()
        sname = self.personalTable.item(row,2).text()
        #获取当前部门

        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        sql = "select d.d_name,p.p_name from sp,department as d,professional as p where sp.s_no='%s' and sp.p_no = p.p_no and sp.d_no = d.d_no" % (sno)
        cur.execute(sql)
        result = cur.fetchone()

        predepartment = result[0]
        prepost = result[1]
        print("predepartment"+predepartment)
        print("prepost"+prepost)
        changeDialog = changePersonelDialog(self)


        #填入相应信息
        changeDialog.line_sname.setText(_translate("personalDialog", sname))
        changeDialog.line_sno.setText(_translate("personalDialog", sno))
        changeDialog.line_predepart.setText(_translate("personalDialog", predepartment))
        changeDialog.line_prepost.setText(_translate("personalDialog", prepost))

        changeDialog.show()
        changeDialog.exec_()

    def MenuShow(self):
        try:

            rightMenu = QtWidgets.QMenu(self.personalTable)
            removeAction = QtWidgets.QAction(u"删除", self,triggered=self.deleteItem)  # triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
            rightMenu.addAction(removeAction)

            rightMenu.exec_(QtGui.QCursor.pos())
            print(111)
        except Exception as e:
            print(e)

    def deleteItem(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        row = self.personalTable.currentRow()
        pno = self.personalTable.item(row,0).text()

        print(pno)

        reply = QtWidgets.QMessageBox.question(self, '提示框',
                                     "确定要删除这条数据吗?", QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            #print("yes")
            sql = "delete from personnel where p_no = '%s'" %(pno)
            try:
                print(sql)
                cur.execute(sql)
            except Exception as e:
                print(e)

            self.personalTable.removeRow(row)

            db.commit()
        else:
            return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainMindow = personnel_history()
    mainMindow.show()
    sys.exit(app.exec_())
