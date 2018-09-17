# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salaryTable.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

#当前薪资和发放

import sys
import pymysql
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class salaryNow(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, salary):
        salary.setObjectName("salary")
        salary.resize(996, 813)
        self.gridLayoutWidget = QtWidgets.QWidget(salary)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 470, 850, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_prededuct = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_prededuct.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.lineEdit_prededuct.setObjectName("lineEdit_prededuct")
        self.gridLayout.addWidget(self.lineEdit_prededuct, 0, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setEnabled(True)
        self.label_5.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setEnabled(True)
        self.label_8.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setEnabled(True)
        self.label_6.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.lineEdit_preprize = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_preprize.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.lineEdit_preprize.setObjectName("lineEdit_preprize")
        self.gridLayout.addWidget(self.lineEdit_preprize, 0, 4, 1, 1)
        self.changebutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.changebutton.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.changebutton.setObjectName("changebutton")
        self.gridLayout.addWidget(self.changebutton, 1, 7, 1, 1)
        self.lineEdit_presalary = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_presalary.setEnabled(True)
        self.lineEdit_presalary.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.lineEdit_presalary.setObjectName("lineEdit_presalary")
        self.gridLayout.addWidget(self.lineEdit_presalary, 0, 2, 1, 1)
        self.lineEdit_afterdeduct = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_afterdeduct.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.lineEdit_afterdeduct.setObjectName("lineEdit_afterdeduct")
        self.gridLayout.addWidget(self.lineEdit_afterdeduct, 1, 6, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setEnabled(True)
        self.label_12.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setEnabled(True)
        self.label_11.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 3, 1, 1)
        self.lineEdit_afterprize = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_afterprize.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.lineEdit_afterprize.setObjectName("lineEdit_afterprize")
        self.gridLayout.addWidget(self.lineEdit_afterprize, 1, 4, 1, 1)
        self.lineEdit_aftersalary = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_aftersalary.setEnabled(True)
        self.lineEdit_aftersalary.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.lineEdit_aftersalary.setObjectName("lineEdit_aftersalary")
        self.gridLayout.addWidget(self.lineEdit_aftersalary, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setEnabled(True)
        self.label_10.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setEnabled(True)
        self.label_9.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setEnabled(True)
        self.label_7.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(salary)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 440, 431, 35))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setEnabled(True)
        self.label.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_sno = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_sno.setEnabled(True)
        self.label_sno.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 18pt \"Adobe Arabic\";")
        self.label_sno.setObjectName("label_sno")
        self.gridLayout_2.addWidget(self.label_sno, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_sname = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_sname.setEnabled(True)
        self.label_sname.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 14pt \"Adobe Arabic\";")
        self.label_sname.setObjectName("label_sname")
        self.gridLayout_2.addWidget(self.label_sname, 1, 3, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(salary)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 5, 860, 430))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        #self.comboBox.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 3, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        #self.searchButton.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_3.addWidget(self.searchButton, 0, 2, 1, 1)
        self.searchText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.searchText.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.searchText.setText("")
        self.searchText.setObjectName("searchText")
        self.gridLayout_3.addWidget(self.searchText, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setStyleSheet("font: 30pt \"Adobe Arabic\";")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.salaryTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.salaryTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.salaryTable.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.salaryTable.setEnabled(True)
        self.salaryTable.setTabletTracking(False)
        self.salaryTable.setAcceptDrops(False)
        self.salaryTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.salaryTable.setStyleSheet("")
        self.salaryTable.setAlternatingRowColors(True)
        self.salaryTable.setShowGrid(True)
        self.salaryTable.setWordWrap(False)
        self.salaryTable.setCornerButtonEnabled(True)
        self.salaryTable.setObjectName("salaryTable")
        self.salaryTable.setColumnCount(8)
        self.salaryTable.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.salaryTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.salaryTable.setHorizontalHeaderItem(7, item)
        self.salaryTable.horizontalHeader().setVisible(True)
        self.salaryTable.horizontalHeader().setCascadingSectionResizes(False)
        self.salaryTable.horizontalHeader().setHighlightSections(True)
        self.salaryTable.horizontalHeader().setSortIndicatorShown(False)
        self.salaryTable.horizontalHeader().setStretchLastSection(True)
        self.salaryTable.verticalHeader().setVisible(False)
        self.salaryTable.verticalHeader().setCascadingSectionResizes(False)
        self.salaryTable.verticalHeader().setSortIndicatorShown(False)
        self.salaryTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.salaryTable)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setStyleSheet("font: 10pt \"Adobe Arabic\";")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)
        self.payrollButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.payrollButton.setStyleSheet("background-color:rgb(255, 57, 60);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Adobe Arabic\";\n"
"")
        self.payrollButton.setObjectName("payrollButton")
        self.gridLayout_5.addWidget(self.payrollButton, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)

        self.retranslateUi(salary)
        QtCore.QMetaObject.connectSlotsByName(salary)

        self.lineEdit_prededuct.setFocusPolicy(False)
        self.lineEdit_preprize.setFocusPolicy(False)
        self.lineEdit_presalary.setFocusPolicy(False)

        self.readMysql()
        self.searchButton.clicked.connect(self.searchRecord)
        self.searchText.editingFinished.connect(self.searchRecord)
        self.salaryTable.clicked.connect(self.setInfo)
        self.changebutton.clicked.connect(self.changeInfo)
        self.payrollButton.clicked.connect(self.payRollForAll)

        #右键发工资
        self.salaryTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.salaryTable.customContextMenuRequested[QtCore.QPoint].connect(self.MenuShow)

    def retranslateUi(self, salary):
        _translate = QtCore.QCoreApplication.translate
        salary.setWindowTitle(_translate("salary", "Form"))
        self.lineEdit_prededuct.setText(_translate("salary", ""))
        self.label_5.setText(_translate("salary", "底薪："))
        self.label_8.setText(_translate("salary", "应扣工资："))
        self.label_6.setText(_translate("salary", "奖金："))
        self.lineEdit_preprize.setText(_translate("salary", ""))
        self.changebutton.setText(_translate("salary", "确定修改"))
        self.lineEdit_presalary.setText(_translate("salary", ""))
        self.lineEdit_afterdeduct.setText(_translate("salary", ""))
        self.label_12.setText(_translate("salary", "应扣工资："))
        self.label_11.setText(_translate("salary", "奖金："))
        self.lineEdit_afterprize.setText(_translate("salary", ""))
        self.lineEdit_aftersalary.setText(_translate("salary", ""))
        self.label_10.setText(_translate("salary", "底薪："))
        self.label_9.setText(_translate("salary", "调整后："))
        self.label_7.setText(_translate("salary", "调整前："))
        self.label.setText(_translate("salary", "工号："))
        self.label_sno.setText(_translate("salary", ""))
        self.label_2.setText(_translate("salary", "姓名："))
        self.label_sname.setText(_translate("salary", ""))
        self.comboBox.setItemText(0, _translate("salary", "按姓名查找"))
        self.comboBox.setItemText(1, _translate("salary", "按工号查找"))
        self.comboBox.setItemText(2, _translate("salary", "按部门查找"))
        self.searchButton.setText(_translate("salary", "查询"))
        self.salaryTable.setSortingEnabled(False)
        item = self.salaryTable.verticalHeaderItem(0)
        item.setText(_translate("salary", "New Row"))
        item = self.salaryTable.verticalHeaderItem(1)
        item.setText(_translate("salary", "New Row"))
        item = self.salaryTable.verticalHeaderItem(2)
        item.setText(_translate("salary", "New Row"))
        item = self.salaryTable.verticalHeaderItem(3)
        item.setText(_translate("salary", "New Row"))
        item = self.salaryTable.horizontalHeaderItem(0)
        item.setText(_translate("salary", "员工编号"))
        item = self.salaryTable.horizontalHeaderItem(1)
        item.setText(_translate("salary", "姓名"))
        item = self.salaryTable.horizontalHeaderItem(2)
        item.setText(_translate("salary", "性别"))
        item = self.salaryTable.horizontalHeaderItem(3)
        item.setText(_translate("salary", "部门"))
        item = self.salaryTable.horizontalHeaderItem(4)
        item.setText(_translate("salary", "职位"))
        item = self.salaryTable.horizontalHeaderItem(5)
        item.setText(_translate("salary", "底薪"))
        item = self.salaryTable.horizontalHeaderItem(6)
        item.setText(_translate("salary", "奖金"))
        item = self.salaryTable.horizontalHeaderItem(7)
        item.setText(_translate("salary", "应扣工资"))
        self.payrollButton.setToolTip(_translate("salary", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.payrollButton.setText(_translate("salary", "一键发工资"))

    def readMysql(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,salary,prize,deduct  from current_salary as c,staff as s,sp,department,professional "+\
              " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no order by (c.s_no+0) desc"

        try:
           cur.execute(sql)
        except Exception as e:
            print(e)
        len = cur.fetchall().__len__()

        cur.execute(sql)
        self.salaryTable.setRowCount(len)

        k = 0
        for i in cur:
            w = 0
            for j in i:
                newItem = QtWidgets.QTableWidgetItem(str(j))
                self.salaryTable.setItem(k, w, newItem)
                w += 1
            k += 1

        cur.close()
        db.close()

    def searchRecord(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        if (self.searchText.text() == ""):
            sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,salary,prize,deduct  from current_salary as c,staff as s,sp,department,professional " + \
                  " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no order by (c.s_no+0) desc"

            cur.execute(sql)
            len = cur.fetchall().__len__()

            cur.execute(sql)
            self.salaryTable.setRowCount(len)

            k = 0
            for i in cur:
                w = 0
                for j in i:
                    newItem = QtWidgets.QTableWidgetItem(str(j))
                    self.salaryTable.setItem(k, w, newItem)
                    w += 1
                k += 1
            return

        # 输入框内容

        temp = self.searchText.text()

        s = '%' + temp + '%'

        # 分类查询
        conditionChoice = self.comboBox.currentText()

        if (conditionChoice == "按姓名查找"):
            sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,salary,prize,deduct  from current_salary as c,staff as s,sp,department,professional " + \
                  " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no "+\
                  " and s.s_name LIKE '%s' order by (c.s_no+0) desc" %(s)

        elif (conditionChoice == "按工号查找"):
            sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,salary,prize,deduct  from current_salary as c,staff as s,sp,department,professional " + \
                  " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no " + \
                  " and s.s_no LIKE '%s' order by (c.s_no+0) desc" % (s)

        elif (conditionChoice == "按部门查找"):
            sql = "select c.s_no,s.s_name,s.s_sex,department.d_name,professional.p_name,salary,prize,deduct  from current_salary as c,staff as s,sp,department,professional " + \
                  " where c.s_no = s.s_no and c.s_no = sp.s_no and sp.p_no = professional.p_no and sp.d_no = department.d_no " + \
                  " and department.d_name LIKE '%s' order by (c.s_no+0) desc" % (s)

        self.salaryTable.clearContents()
        # 清空表格

        # 重新查找后生成表格
        cur.execute(sql)
        len = cur.fetchall().__len__()

        cur.execute(sql)
        self.salaryTable.setRowCount(len)

        k = 0
        for i in cur:
            w = 0
            for j in i:
                newItem = QtWidgets.QTableWidgetItem(str(j))
                self.salaryTable.setItem(k, w, newItem)
                w += 1
            k += 1

        if (self.searchText.text() == ""):
            pass

        cur.close()
        db.close()

    def setInfo(self):
        row = self.salaryTable.currentRow()
        s_no = self.salaryTable.item(row, 0).text()
        s_name = self.salaryTable.item(row, 1).text()

        presalary = self.salaryTable.item(row, 5).text()
        preprize = self.salaryTable.item(row, 6).text()
        prededuct = self.salaryTable.item(row, 7).text()

        self.label_sno.setText(s_no)
        self.label_sname.setText(s_name)
        self.lineEdit_presalary.setText(presalary)
        self.lineEdit_preprize.setText(preprize)
        self.lineEdit_prededuct.setText(prededuct)

    #修改薪资
    def changeInfo(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        sno = self.label_sno.text()

        aftersalary = self.lineEdit_aftersalary.text()
        afterprize = self.lineEdit_afterprize.text()
        afterdeduct = self.lineEdit_afterdeduct.text()

        if sno == "":
            QtWidgets.QMessageBox.question(self, '提示框',
                                           "你并未选择员工！", QtWidgets.QMessageBox.Yes )
            return

        if aftersalary == "" or afterprize == "" or afterdeduct == "":
            reply = QtWidgets.QMessageBox.question(self, '提示框',
                                                   "你还有信息未填?", QtWidgets.QMessageBox.Yes )

        else:
            reply = QtWidgets.QMessageBox.question(self, '提示框',
                                                   "你确定要修改吗?", QtWidgets.QMessageBox.Yes |
                                                   QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:

                sql = "update current_salary set salary = '%s' , prize = '%s',deduct = '%s' where s_no = '%s'" % (aftersalary,afterprize,afterdeduct,sno)
                try:
                    cur.execute(sql)
                    QtWidgets.QMessageBox.question(self, '提示框',
                                                   "修改成功！！！", QtWidgets.QMessageBox.Yes )
                except Exception as e:
                    print(e)

                db.commit()

                self.searchRecord()

                self.lineEdit_afterdeduct.setText("")
                self.lineEdit_afterprize.setText("")
                self.lineEdit_aftersalary.setText("")

                self.lineEdit_presalary.setText(aftersalary)
                self.lineEdit_prededuct.setText(afterdeduct)
                self.lineEdit_preprize.setText(afterprize)
                return
            else:
                return

    #一键发工资
    def payRollForAll(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        reply = QtWidgets.QMessageBox.question(self, '提示框',
                                               "确定要给所有员工发工资吗？", QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            s_date = datetime.datetime.now().strftime('%Y-%m-%d')
            year_month = datetime.datetime.now().strftime('%Y-%m')

            rows = self.salaryTable.rowCount()

            cur.execute("select sa_no from salary order by (sa_no+0) desc ")
            result = cur.fetchone()
            len = int(result[0])

            totalSalary = 0
            for row in range(0,rows):
                s_no = self.salaryTable.item(row, 0).text()

                s_date = datetime.datetime.now().strftime('%Y-%m-%d')
                year_month = datetime.datetime.now().strftime('%Y-%m')
                leastpays = self.salaryTable.item(row, 5).text()
                prize = self.salaryTable.item(row, 6).text()
                deduct = self.salaryTable.item(row, 7).text()

                sql = "select c_ldays,c_odays,c_adays from checking " + \
                      "where s_no = '%s' and c_date = '%s'" % (s_no, year_month)
                # c_ldays 请假日 ,c_odays 加班日,c_adays 矿工日

                statu = cur.execute(sql)
                print(statu)
                if statu == 0:
                    c_ldays = float(0)
                    c_odays = float(0)
                    c_adays = float(0)
                else:
                    result = cur.fetchone()
                    c_ldays = float(result[0])
                    c_odays = float(result[1])
                    c_adays = float(result[2])

                print(c_ldays)

                deduct = float(deduct) + c_adays * 150 + c_ldays * 20
                # 矿工一天扣150，请假一天20

                doublingpays = c_odays * 130
                # 加班一天130

                # 养老金
                dkannuity = float(leastpays) * 0.08
                # 医疗保险
                dkinsurrance = float(leastpays) * 0.02
                # 实际获得工资
                real_salary = float(leastpays) + float(prize) + doublingpays - dkannuity - dkinsurrance - deduct
                totalSalary += real_salary

                # 获取当前流水号的最大值
                len += 1
                sa_no = str(len)

                sql = "insert into salary values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                      % (sa_no, s_no, leastpays, prize, doublingpays, dkannuity, dkinsurrance, s_date, deduct, real_salary)
                cur.execute(sql)
                db.commit()

        QtWidgets.QMessageBox.question(self, '提示框',
                                       "已发工资，工资总计:%s元" % (totalSalary), QtWidgets.QMessageBox.Yes)
        cur.close()
        db.close()

    #右键发工资
    def MenuShow(self):
        try:

            rightMenu = QtWidgets.QMenu(self.salaryTable)
            removeAction = QtWidgets.QAction(u"发工资", self,
                                             triggered=self.payRoll)  # triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
            rightMenu.addAction(removeAction)

            rightMenu.exec_(QtGui.QCursor.pos())

        except Exception as e:
            print(e)

    def payRoll(self):
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        row = self.salaryTable.currentRow()
        s_no = self.salaryTable.item(row, 0).text()
        s_name  = self.salaryTable.item(row, 1).text()

        reply = QtWidgets.QMessageBox.question(self, '提示框',
                                               "确定要给工号%s,姓名%s的员工发工资吗？"%(s_no,s_name), QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            s_date = datetime.datetime.now().strftime('%Y-%m-%d')
            year_month = datetime.datetime.now().strftime('%Y-%m')
            leastpays = self.salaryTable.item(row, 5).text()
            prize = self.salaryTable.item(row,6).text()
            deduct = self.salaryTable.item(row,7).text()

            sql = "select c_ldays,c_odays,c_adays from checking "+\
                  "where s_no = '%s' and c_date = '%s'" % (s_no,year_month)
            #c_ldays 请假日 ,c_odays 加班日,c_adays 矿工日

            statu = cur.execute(sql)
            if statu == 0:
                c_ldays = float(0)
                c_odays = float(0)
                c_adays = float(0)
            else:
                result = cur.fetchone()
                c_ldays = float(result[0])
                c_odays = float(result[1])
                c_adays = float(result[2])
            print(c_ldays)

            deduct = float(deduct) + c_adays * 150 + c_ldays * 20
            # 矿工一天扣150，请假一天20

            doublingpays = c_odays * 130
            # 加班一天130

            # 养老金
            dkannuity = float(leastpays) * 0.08
            # 医疗保险
            dkinsurrance = float(leastpays) * 0.02
            # 实际获得工资

            real_salary = float(leastpays) + float(prize) + doublingpays - dkannuity - dkinsurrance - deduct
            print(real_salary)

            #获取当前流水号的最大值
            cur.execute("select sa_no from salary order by (sa_no+0) desc ")
            len = cur.fetchone()
            sa_no = str(int(len[0]) + 1)

            sql = "insert into salary values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
                  %(sa_no,s_no,leastpays,prize,doublingpays,dkannuity,dkinsurrance,s_date,deduct,real_salary)
            cur.execute(sql)
            db.commit()

            QtWidgets.QMessageBox.question(self, '提示框',
                                           "已发工资,流水号%s,工资%s" % (sa_no,real_salary), QtWidgets.QMessageBox.Yes)

        cur.close()
        db.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainMindow = salaryNow()
    mainMindow.show()
    sys.exit(app.exec_())