# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personalDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

#人员调动修改对话框

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pymysql
import datetime

class changePersonelDialog(QtWidgets.QDialog):
    add_info_success_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(changePersonelDialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, personalDialog):
        personalDialog.setObjectName("personalDialog")
        personalDialog.resize(400, 470)
        self.gridLayoutWidget = QtWidgets.QWidget(personalDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 350, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_prepost = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_prepost.setScaledContents(False)
        self.label_prepost.setObjectName("label_prepost")
        self.gridLayout.addWidget(self.label_prepost, 3, 0, 1, 1)
        self.comboxdepart = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboxdepart.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.comboxdepart.setObjectName("comboxdepart")

        self.gridLayout.addWidget(self.comboxdepart, 4, 1, 1, 1)
        self.label_afterdepart = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_afterdepart.setScaledContents(False)
        self.label_afterdepart.setObjectName("label_afterdepart")
        self.gridLayout.addWidget(self.label_afterdepart, 4, 0, 1, 1)
        self.line_prepost = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_prepost.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.line_prepost.setObjectName("line_prepost")
        self.gridLayout.addWidget(self.line_prepost, 3, 1, 1, 1)
        self.comboBoxProfession = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBoxProfession.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.comboBoxProfession.setObjectName("comboBoxProfession")

        self.gridLayout.addWidget(self.comboBoxProfession, 5, 1, 1, 1)
        self.label_sno = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sno.setScaledContents(False)
        self.label_sno.setObjectName("label_sno")
        self.gridLayout.addWidget(self.label_sno, 1, 0, 1, 1)
        self.line_sno = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_sno.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.line_sno.setObjectName("line_sno")
        self.gridLayout.addWidget(self.line_sno, 1, 1, 1, 1)
        self.label_predepart = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_predepart.setScaledContents(False)
        self.label_predepart.setObjectName("label_predepart")
        self.gridLayout.addWidget(self.label_predepart, 2, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_name.setScaledContents(False)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.line_sname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_sname.setEnabled(True)
        self.line_sname.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.line_sname.setObjectName("line_sname")
        self.gridLayout.addWidget(self.line_sname, 0, 1, 1, 1)
        self.line_predepart = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_predepart.setStyleSheet("font: 14pt \"Adobe Arabic\";")
        self.line_predepart.setObjectName("line_predepart")
        self.gridLayout.addWidget(self.line_predepart, 2, 1, 1, 1)
        self.label_afterpost = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_afterpost.setScaledContents(False)
        self.label_afterpost.setObjectName("label_afterpost")
        self.gridLayout.addWidget(self.label_afterpost, 5, 0, 1, 1)
        self.button_ok = QtWidgets.QPushButton(personalDialog)
        self.button_ok.setGeometry(QtCore.QRect(100, 410, 221, 41))
        self.button_ok.setStyleSheet("font: 14pt \"Adobe Arabic\";\n"
                                      "color:rgb(255, 0, 0);")
        self.button_ok.setObjectName("button_ok")


        self.line_sname.setFocusPolicy(False)
        self.line_sno.setFocusPolicy(False)
        self.line_prepost.setFocusPolicy(False)
        self.line_predepart.setFocusPolicy(False)

        self.retranslateUi(personalDialog)
        self.button_ok.clicked.connect(self.clickOk)

        QtCore.QMetaObject.connectSlotsByName(personalDialog)

    def retranslateUi(self, personalDialog):
        _translate = QtCore.QCoreApplication.translate
        personalDialog.setWindowTitle(_translate("personalDialog", "人员调动"))
        self.label_prepost.setText(_translate("personalDialog", "<html><head/><body><p><span style=\" font-size:18pt;\">原职位：</span></p></body></html>"))

        self.label_afterdepart.setText(_translate("personalDialog", "<html><head/><body><p><span style=\" font-size:18pt;\">调入部门：</span></p></body></html>"))
        self.line_prepost.setText(_translate("personalDialog", "453"))

        self.label_sno.setText(_translate("personalDialog", "<html><head/><body><p><span style=\" font-size:18pt;\">工号：</span></p></body></html>"))
        self.line_sno.setText(_translate("personalDialog", "20001"))
        self.label_predepart.setText(_translate("personalDialog", "<html><head/><body><p><span style=\" font-size:18pt;\">原部门：</span></p></body></html>"))
        self.label_name.setText(_translate("personalDialog", "<html><head/><body><p><span style=\" font-size:18pt;\">姓名：</span></p></body></html>"))
        self.line_sname.setText(_translate("personalDialog", "xxx"))
        self.line_predepart.setText(_translate("personalDialog", "53"))
        self.label_afterpost.setText(_translate("personalDialog", "<html><head/><body><p><span style=\" font-size:18pt;\">调入职位：</span></p></body></html>"))
        self.button_ok.setText(_translate("personalDialog", "保存修改"))
        self.initcombox()

    #下拉列表
    def initcombox(self):
        _translate = QtCore.QCoreApplication.translate
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")

        cur = db.cursor()
        sql = "SELECT d_name from department"
        cur.execute(sql)

        index = 0
        for i in cur:
            for j in i:
                print(str(j))
                self.comboxdepart.insertItem(index,j)

        sql = "SELECT p_name from professional"
        cur.execute(sql)

        index = 0
        for i in cur:
            for j in i:
                self.comboBoxProfession.insertItem(index, j)


    #确定提交后
    def clickOk(self):

        reply = QtWidgets.QMessageBox.question(self, '提示框',
                                     "确定保存修改吗?", QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.No:
            return

        #判断输入字段是否为空
        afterdepart = self.comboxdepart.currentText()
        afterpost = self.comboBoxProfession.currentText()

        print(afterdepart)
        print(afterpost)

        sno = self.line_sno.text()
        predepartt = self.line_predepart.text()
        prepost = self.line_prepost.text()
        db = pymysql.connect("localhost", "root", "123456", db="personnel_man")
        cur = db.cursor()

        p_date = datetime.datetime.now().strftime('%Y-%m-%d')


        cur.execute("select d_no from department where d_name = '%s' "%(afterdepart))
        result = cur.fetchone()
        d_no = str(result[0])

        cur.execute("select p_no from professional where p_name = '%s' " % (afterpost))
        result = cur.fetchone()
        p_no = str(result[0])

        #判断当前部门是否有经理
        sql = "select * from sp where d_no = '%s' and p_no='%s'"%(d_no,p_no)
        sta = cur.execute(sql)
        print(sta)

        #调整前是经理，或者调整后是经理，更改数据库
        if prepost == '经理':
            print(111111111111111111111,prepost)
            sql = "update department set s_no=NULL where d_no = '%s'" % (d_no)
            cur.execute(sql)
            db.commit()
        if afterpost == '经理':
            sql = "update department set s_no='%s' where d_no = '%s'" % (sno, d_no)
            cur.execute(sql)
            db.commit()
            if sta != 0:
                reply = QtWidgets.QMessageBox.question(self, '提示框',
                                                       "%s已有经理，无法进行该操作" % (afterdepart), QtWidgets.QMessageBox.Yes)
                return

        #更新sp就职表
        sql = "update sp set d_no='%s',p_no = '%s',entry_time = '%s' where s_no = '%s'"%(d_no,p_no,p_date,sno)
        cur.execute(sql)
        db.commit()

        #更新人事调动表
        try:
            cur.execute("select p_no from personnel order by (p_no+0) desc ")
            len = cur.fetchone()
            if len == None:
                p_no = 1
            else:
                p_no = str(int(len[0])+1)

        except Exception as e:
            print(e)

        sql = "insert into personnel value ('%s','%s','%s','%s','%s','%s','%s')" % (
        p_no, sno, predepartt, afterdepart, prepost, afterpost, p_date)
        sta = cur.execute(sql)
        if sta == 1:
            print("修改成功")
        else:
            print("false")
        db.commit()

        cur.close()
        db.close()
        self.add_info_success_signal.emit()
        self.close()
        return

'''
    def closeEvent(self, event):

        reply = QtWidgets.QMessageBox.question(self, '提示框',
                                     "确定不保存修改退出吗?", QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainMindow = changePersonelDialog()
    mainMindow.show()
    sys.exit(app.exec_())