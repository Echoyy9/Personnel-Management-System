import  sys
import  pymysql
import time
import re
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QAction,QMenu,QAbstractItemView
from mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt,QPoint

from dept import Ui_Form
from addstaff import Ui_add_staff
from delete_staff import  Ui_delete_staff
from find_staff import  Ui_find_staff
from alter_staff import Ui_alter_staff
from alter_display_staff import Ui_alter_display_staff
from staff_detail import Ui_staff_detail

from alter_dept import Ui_alter_dept
from alter_display_dept import  Ui_alter_display_dept
from add_dept import  Ui_add_dept
from delete_dept import Ui_delete_dept
from find_dept import Ui_find_dept
from dept_detail import Ui_dept_detail
from PyQt5.QtGui import QCursor
from profess import  Ui_profess
from add_profess import  Ui_add_profess
from alter_profess import  Ui_alter_profess
from functools import partial
from login import  Ui_login
from admin import  Ui_admin
from add_admin import  Ui_add_admin
from alter_admin import  Ui_alter_admin
import sip

#薪资
from salaryHistoryTable import salaryHistory
from salaryNowTable import  salaryNow

#人事
from personalHistory import personnel_history
from personalNow import  personnel_now

#考核
from checkTable import checkHistory
from checkChange import checkChange


#主界面
class staff_Admin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(staff_Admin, self).__init__()
        self.setupUi(self)
        grid = QtWidgets.QGridLayout()
        self.content.setLayout(grid)

    def test(self):
        self.label1.show()
        self.label2.show()
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        txt = self.treeWidget.currentItem().text(0)
        grid = self.content.layout()

        if txt!='部门信息' and txt!='考核管理' and txt!='人事管理' and txt!='薪资管理' and txt!='员工信息':
            for singer_obj in self.content.children():
                #print("初始",singer_obj)
                if(isinstance(singer_obj,QtWidgets.QLabel)==False and isinstance(singer_obj,QtWidgets.QGridLayout)==False):
                    grid.removeWidget(singer_obj)
                    singer_obj.deleteLater()
                    sip.delete(singer_obj)
        else:
            self.label1.hide()
            self.label2.hide()

        if txt == '添加员工信息':
            self.label1.hide()
            self.label2.hide()
            self.add_staff_page = add_staff()
            grid.addWidget(self.add_staff_page)
        elif txt =='修改员工信息':
            self.label1.hide()
            self.label2.hide()
            self.alter_display_staff_page = alter_display_staff()
            grid.addWidget(self.alter_display_staff_page)
            obj={}
            # 打开数据库
            cursor = db.cursor()
            try:
                cursor.execute(" select staff.s_no,staff.s_name,department.d_name from staff, department,sp where sp.s_no = staff.s_no and department.d_no = sp.d_no order by convert (staff.s_no,signed)")
                results = cursor.fetchall()
               # print(results)

                for row in results:
                    sno = row[0]
                    sname = row[1]
                    dname = row[2]
                    oldrow = self.alter_display_staff_page.tableWidget.rowCount()


                    self.alter_display_staff_page.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(sno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 1, item)

                    item = QTableWidgetItem(dname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_staff_page.tableWidget.setItem(oldrow, 2, item)

                    '''
                    btn = QtWidgets.QPushButton()
                    btn.setText("修改信息")
                    btn.setStyleSheet("text-decoration: underline")
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                    btn.clicked.connect(self.alter_display_staff_page.btnclicked)
                    #btn.setGeometry(QtCore.QRect(0,0, 75, 23))
                    #item = QTableWidgetItem()
                    #btn.setStyleSheet("background:red")
                    self.alter_display_staff_page.tableWidget.setCellWidget(oldrow,3,btn)
                    '''
                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                    obj[strbtn].setText("修改信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")
                    self.alter_display_staff_page.one = partial(self.alter_display_staff_page.btnclicked, obj[strbtn])
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.alter_display_staff_page.tableWidget.setCellWidget(oldrow, 3, obj[strbtn])
                    obj[strbtn].clicked.connect(self.alter_display_staff_page.one)
                   # btn.click

            except:
                print("error")
        elif txt=='删除员工信息':
            self.label1.hide()
            self.label2.hide()
            self.delete_staff_page = delete_staff()
            grid.addWidget(self.delete_staff_page)
            obj={}
            # 打开数据库
            cursor = db.cursor()
            try:
                cursor.execute(" select staff.s_no,staff.s_name,department.d_name from staff, department,sp where sp.s_no = staff.s_no and department.d_no = sp.d_no order by convert (staff.s_no,signed)")
                results = cursor.fetchall()
                #print(results)

                for row in results:
                    sno = row[0]
                    sname = row[1]
                    dname = row[2]
                    oldrow = self.delete_staff_page.tableWidget.rowCount()
                    self.delete_staff_page.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(sno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.delete_staff_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.delete_staff_page.tableWidget.setItem(oldrow, 1, item)

                    item = QTableWidgetItem(dname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.delete_staff_page.tableWidget.setItem(oldrow, 2, item)
                    '''
                    btn = QtWidgets.QPushButton()
                    btn.setText("删除该员工")
                    btn.setStyleSheet("text-decoration: underline")
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                    btn.clicked.connect(self.delete_staff_page.btnclicked)
                    #btn.setGeometry(QtCore.QRect(0,0, 75, 23))
                    #item = QTableWidgetItem()
                    #btn.setStyleSheet("background:red")
                    self.delete_staff_page.tableWidget.setCellWidget(oldrow,3,btn)
                   # btn.click
                '''
                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                    obj[strbtn].setText("删除员工")
                    obj[strbtn].setStyleSheet("text-decoration: underline")
                    self.delete_staff_page.one = partial(self.delete_staff_page.btnclicked, obj[strbtn])
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.delete_staff_page.tableWidget.setCellWidget(oldrow, 3, obj[strbtn])
                    obj[strbtn].clicked.connect(self.delete_staff_page.one)

            except:
                print("error")
        elif txt=='查询员工信息':
            self.label1.hide()
            self.label2.hide()
            self.find_staff_page = find_staff()
            grid.addWidget(self.find_staff_page)
            obj={}
            # 打开数据库
            cursor = db.cursor()
            try:
                cursor.execute("select s_no,s_name from staff order by convert (s_no,signed)")
                results = cursor.fetchall()

                for row in results:
                    sno = row[0]
                    sname = row[1]

                    oldrow = self.find_staff_page.tableWidget.rowCount()
                    self.find_staff_page.tableWidget.setRowCount(oldrow + 1)

                    item = QTableWidgetItem(str(sno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.find_staff_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.find_staff_page.tableWidget.setItem(oldrow, 1, item)

                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()


                    obj[strbtn].setText("详细信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")

                    self.find_staff_page.one = partial(self.find_staff_page.btnclicked, obj[strbtn])
                    #print(btn.objectName())
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.find_staff_page.tableWidget.setCellWidget(oldrow,2,obj[strbtn])
                    obj[strbtn].clicked.connect(self.find_staff_page.one)


            except:
                print("error")
        elif txt == '修改部门信息':
            self.label1.hide()
            self.label2.hide()
            self.alter_display_dept_page = alter_display_dept()
            grid.addWidget(self.alter_display_dept_page)
            obj={}
            # 打开数据库
            cursor = db.cursor()
            try:
                cursor.execute(
                    " select d_no,d_name,s_no from department order by convert (d_no,signed)")
                results = cursor.fetchall()
                #print(results)

                for row in results:
                    dno = row[0]
                    dname = row[1]
                    sno = row[2]
                    #print(dno,dname,sno)

                    if sno==None:
                        sname='暂无'
                    else:
                        cursor.execute("select s_name from staff where s_no='%s'"%(sno))
                        result = cursor.fetchone()
                        sname = result[0]
                    #print(sname)
                    
                    oldrow = self.alter_display_dept_page.tableWidget.rowCount()

                    self.alter_display_dept_page.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(dno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_dept_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(dname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_dept_page.tableWidget.setItem(oldrow, 1, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.alter_display_dept_page.tableWidget.setItem(oldrow, 2, item)
                    '''
                    btn = QtWidgets.QPushButton()
                    btn.setText("修改信息")
                    btn.setStyleSheet("text-decoration: underline")
                    btn.clicked.connect(self.alter_display_dept_page.btnclicked)
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                    self.alter_display_dept_page.tableWidget.setCellWidget(oldrow, 3, btn)
                '''
                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                    obj[strbtn].setText("修改信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")

                    self.alter_display_dept_page.one = partial(self.alter_display_dept_page.btnclicked, obj[strbtn])
                    # print(btn.objectName())
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.alter_display_dept_page.tableWidget.setCellWidget(oldrow, 3, obj[strbtn])
                    obj[strbtn].clicked.connect(self.alter_display_dept_page.one)

                # btn.click

            except:
                print("error")
        elif txt == '查询部门信息':
            self.label1.hide()
            self.label2.hide()
            self.find_dept_page = find_dept()
            grid.addWidget(self.find_dept_page)
            obj={}
            # 打开数据库
            cursor = db.cursor()
            try:
                cursor.execute("select d_no,d_name from department order by convert(d_no,signed)")
                results = cursor.fetchall()
                #print(results)

                for row in results:
                    dno = row[0]
                    dname = row[1]


                    oldrow = self.find_dept_page.tableWidget.rowCount()
                    self.find_dept_page.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(dno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.find_dept_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(dname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.find_dept_page.tableWidget.setItem(oldrow, 1, item)
                    '''
                    btn = QtWidgets.QPushButton()
                    btn.setText("详细信息")
                    btn.setStyleSheet("text-decoration: underline")
                    btn.clicked.connect(self.find_dept_page.btnclicked)
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                    self.find_dept_page.tableWidget.setCellWidget(oldrow, 2, btn)
                   '''
                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                    obj[strbtn].setText("详细信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")
                    self.find_dept_page.one = partial(self.find_dept_page.btnclicked, obj[strbtn])
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.find_dept_page.tableWidget.setCellWidget(oldrow, 2, obj[strbtn])
                    obj[strbtn].clicked.connect(self.find_dept_page.one)

            except:
                print("error")
        elif txt=='删除部门信息':

            self.label1.hide()
            self.label2.hide()
            self.delete_dept_page = delete_dept()
            grid.addWidget(self.delete_dept_page)

            # 打开数据库
            cursor = db.cursor()
            try:
                cursor.execute(
                    " select d_no,d_name,s_no from department order by convert (d_no,signed)")
                results = cursor.fetchall()
                #print("hello",results)
                obj={}
                for row in results:
                    dno = row[0]
                    dname = row[1]
                    sno = row[2]
                    #print(dno, dname, sno)

                    if sno == None:
                        sname = '暂无'
                    else:
                        cursor.execute("select s_name from staff where s_no='%s'" % (sno))
                        result = cursor.fetchone()
                        sname = result[0]
                    #print(sname)

                    oldrow = self.delete_dept_page.tableWidget.rowCount()

                    self.delete_dept_page.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(dno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.delete_dept_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(dname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.delete_dept_page.tableWidget.setItem(oldrow, 1, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.delete_dept_page.tableWidget.setItem(oldrow, 2, item)
                    '''
                    btn = QtWidgets.QPushButton()
                    btn.setText("删除")
                    btn.setStyleSheet("text-decoration: underline")
                    btn.clicked.connect(self.delete_dept_page.btnclicked)
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                    self.delete_dept_page.tableWidget.setCellWidget(oldrow, 3, btn)
                  '''
                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                    obj[strbtn].setText("删除部门")
                    obj[strbtn].setStyleSheet("text-decoration: underline")
                    self.delete_dept_page.one = partial(self.delete_dept_page.btnclicked, obj[strbtn])
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.delete_dept_page.tableWidget.setCellWidget(oldrow, 3, obj[strbtn])
                    obj[strbtn].clicked.connect(self.delete_dept_page.one)
            except:
                print("error")
        elif txt=='添加部门信息':
            self.label1.hide()
            self.label2.hide()
            self.add_dept_page = add_dept()
            grid.addWidget(self.add_dept_page)
        elif txt=="职位信息管理":
            self.label1.hide()
            self.label2.hide()
            self.profess_admin_page= profess_admin()
            grid.addWidget(self.profess_admin_page)

            cursor = db.cursor()
            try:
                cursor.execute("select p_no,p_name from professional")
                results = cursor.fetchall()
                #print("hello", results)

                for row in results:
                    pno = row[0]
                    pname = row[1]
                   # print(pno)
                   # print(pname)

                    oldrow = self.profess_admin_page.tableWidget.rowCount()

                    self.profess_admin_page.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(pno)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.profess_admin_page.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(pname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.profess_admin_page.tableWidget.setItem(oldrow, 1, item)


                    #btn = QtWidgets.QPushButton()
                    #btn.setText("删除")
                    #btn.setStyleSheet("text-decoration: underline")
                    #btn.clicked.connect(self.delete_dept_page.btnclicked)
                    #btn.setCursor(QCursor(Qt.PointingHandCursor))
                    #self.delete_dept_page.tableWidget.setCellWidget(oldrow, 3, btn)
            except:
                print("error")
        elif txt=="管理权限控制":
            self.label1.hide()
            self.label2.hide()
            self.admin_table = admin()
            grid.addWidget(self.admin_table)

            cursor = db.cursor()
            try:
                cursor.execute("select s_no,pwd from admin_table order by convert (s_no,signed)")
                results = cursor.fetchall()
                #print(results)
                for row in results:
                    sno = row[0]
                    pwd = row[1]
                    oldrow = self.admin_table.tableWidget.rowCount()

                    self.admin_table.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(sno)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_table.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(pwd)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_table.tableWidget.setItem(oldrow, 1, item)
            except:
                print("error")
        elif txt == '薪资历史查询':
            self.label1.hide()
            self.label2.hide()
            try:
                self.find_salary_history = find_salary()
                grid.addWidget(self.find_salary_history)
            except Exception as e:
                print(e)

        elif txt == '薪资分配管理':
            self.label1.hide()
            self.label2.hide()
            try:
                self.alter_salary_now = alter_salary()
                grid.addWidget(self.alter_salary_now)
            except Exception as e:
                print(e)

        elif txt == '调动历史查询':
            self.label1.hide()
            self.label2.hide()
            try:
                self.find_personal_history = find_personal()
                grid.addWidget(self.find_personal_history)
            except Exception as e:
                print(e)

        elif txt == '人员调动':
            self.label1.hide()
            self.label2.hide()
            try:
                self.alter_personal_now = alter_personal()
                grid.addWidget(self.alter_personal_now)
            except Exception as e:
                print(e)

        elif txt == '人员考核':
            self.label1.hide()
            self.label2.hide()
            try:
                self.alter_check_now = alter_check()
                grid.addWidget(self.alter_check_now)
            except Exception as e:
                print(e)

        elif txt == '考核历史查询':
            self.label1.hide()
            self.label2.hide()
            try:
                self.find_check_history = find_check()
                grid.addWidget(self.find_check_history)
            except Exception as e:
                print(e)

#登陆
class login(QtWidgets.QDialog,Ui_login):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)

    def jump(self):
        sno = self.sno.text()
        pwd = self.pwd.text()
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
           # print(sno)
            sql = "select count(*) from admin_table where s_no='%s' and pwd='%s'"%(sno,pwd)
            cursor.execute(sql)
            result = cursor.fetchone()
            #print(result)
            count = result[0]
            if count==0:
                QMessageBox.information(self,"提示","用户名或密码错误！",QMessageBox.Yes)
            else:

                self.close()
                self.my_staffAdmin = staff_Admin()
                self.my_staffAdmin.show()

        except:
            print("error")
#职位管理
class profess_admin(QtWidgets.QWidget,Ui_profess):
    def __init__(self):
        super(profess_admin, self).__init__()
        self.setupUi(self)

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
    def generateMenu(self, pos):
        #print(pos)
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        menu = QMenu()
        item1 = menu.addAction("添加")
        item2 = menu.addAction("删除")
        item3 = menu.addAction("修改")
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == item1: #添加
            self.add_profess_page = add_profess(self)
            self.add_profess_page.show()

        elif action == item2:#删除
            row = self.tableWidget.currentRow()
            pno = self.tableWidget.item(row, 0).text()  # 获取工号
            reply = QMessageBox.information(self,"提示","您是否确定要删除该职位?",QMessageBox.Yes|QMessageBox.No)
            if reply == QMessageBox.Yes and row!=0:
                db = pymysql.connect("localhost", "user", "123456", "personnel_man")
                cursor = db.cursor()
                try:
                    cursor.execute("select count(*) from sp where p_no='%s'"%(pno))
                    result = cursor.fetchone()
                    count = result[0]
                    if count==0:
                        sql = "delete from professional where p_no='%s'" %(pno)
                        cursor.execute(sql)
                        db.commit()
                        row = self.tableWidget.currentRow()
                        self.tableWidget.removeRow(row)
                    else:
                        QMessageBox.warning(self,"提示","该职位仍有员工占用，请先进行人事调动!",QMessageBox.Yes)
                except:
                    print("error")

        elif action == item3:#修改
            row = self.tableWidget.currentRow()
            pno = self.tableWidget.item(row,0).text()  # 获取工号
            self.alter_profess_page = alter_profess(self)
            self.alter_profess_page.show()
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:
                sql = "select p_name from professional where p_no = '%s'"%(pno)
                cursor.execute(sql)
                result = cursor.fetchone()
                pname = result[0]
                self.alter_profess_page.pname.setText(pname)
                self.alter_profess_page.no.setText(pno)
                #print(result)
            except:
                print("error1")


        else:
            return

#职位修改
class alter_profess(QtWidgets.QWidget,Ui_alter_profess):
    def __init__(self,professAdmin):
        super(alter_profess, self).__init__()
        self.setupUi(self)
        self.profess_admin = professAdmin
    #保存按钮
    def save(self):
        pno = self.no.text()
        pname = self.pname.text()
        if pname == '':
            QMessageBox.information(self, "提示", "请正确填写名称!", QMessageBox.Yes)
        else:
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:
                print(pname,pno)
                sql = "update professional set p_name='%s' where p_no='%s'"%(pname,pno)
                status = cursor.execute(sql)

                db.commit()
                if status == 1:
                    self.rewirte()

                reply = QMessageBox.information(self, "提示", "保存成功！", QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    self.close()
                #self.pname.setText('')
            except:
                print("error")
    #重写表格
    def rewirte(self):
        professA = self.profess_admin
        rows = professA.tableWidget.rowCount()
        i = rows
        while i > 0:
            professA.tableWidget.removeRow(i)
            i = i - 1

        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute("select p_no,p_name from professional order by convert(p_no,signed)")
            results = cursor.fetchall()
            for row in results:
                pno = row[0]
                pname = row[1]
                oldrow = professA.tableWidget.rowCount()
                #print('oldrow=', oldrow)
                professA.tableWidget.setRowCount(oldrow + 1)
                item = QTableWidgetItem(pno)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 0, item)

                item = QTableWidgetItem(pname)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 1, item)
        except:
            print("error")
#职位增加
class add_profess(QtWidgets.QWidget,Ui_add_profess):
    def __init__(self,professAdmin):
        super(add_profess, self).__init__()
        self.setupUi(self)
        self.profess_admin = professAdmin
    #添加按钮
    def add(self):
        pname = self.pname.text()
        if pname=='':
            QMessageBox.information(self,"提示","请正确填写名称!",QMessageBox.Yes)
        else:
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:
                sql = "select max(convert(p_no,signed)) from professional"
                cursor.execute(sql)
                result = cursor.fetchone()
                maxpno = result[0]
                if maxpno == None:
                    newpno = 1
                else:
                    newpno = int(maxpno) + 1

                needstr = ''
                if len(str(newpno)) < 6:
                    need = 6 - len(str(newpno))
                    print(need)
                    for i in range(need):
                        needstr += '0'
                newpno = needstr + str(newpno)

                #print(newpno,pname)
                sql = "insert into professional values('%s','%s')"%(str(newpno),pname)
                status = cursor.execute(sql)
                db.commit()
                if status==1:
                    self.rewrite()
                reply = QMessageBox.information(self,"提示","添加成功！",QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    self.close()
            except:
                print("error")
    #重写表格
    def rewrite(self):
        professA = self.profess_admin
        rows = professA.tableWidget.rowCount()
        i=rows
        while i>0:
            professA.tableWidget.removeRow(i)
            i=i-1
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute("select p_no,p_name from professional order by convert(p_no,signed)")
            results = cursor.fetchall()
            #print("hello", results)
            for row in results:
                pno = row[0]
                pname = row[1]
                oldrow =professA.tableWidget.rowCount()
                #print('oldrow=',oldrow)
                professA.tableWidget.setRowCount(oldrow + 1)
                item = QTableWidgetItem(pno)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 0, item)
                
                item = QTableWidgetItem(pname)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 1, item)
        except:
            print("error")

#部门信息表
class dept_Info(QtWidgets.QTableWidget,Ui_Form):
    def __init__(self):
        super(dept_Info, self).__init__()
        self.setupUi(self)

#增加员工信息
class add_staff(QtWidgets.QWidget,Ui_add_staff):
    def __init__(self):
        super(add_staff, self).__init__()
        self.setupUi(self)
        self.label_school.hide()
        self.school.hide()
        self.label_time.hide()
        self.graduate_time.hide()
        self.label_major.hide()
        self.major.hide()

        self.department.addItem("-请选择")
        self.professional.addItem("-请选择")
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            sql = "select d_name from department"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                dname = row[0]
                self.department.addItem(dname)

            sql = "select p_name from professional"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                pname = row[0]
                self.professional.addItem(pname)
        except:
            print("error")

        #self.isMarried.setCurrentText("")
    def addInfo(self):

        #sno = self.no.text()
        name = self.name.text()
        sex = self.sex.currentText()
        birth = self.birth.text()
        tel = self.tel.text()
        address = self.address.text()
        isMarried = self.isMarried.currentText()
        email = self.email.text()
        identity = self.identity.text()
        department = self.department.currentText()
        professional = self.professional.currentText()
        entry_time = self.entry_time.text()
        salary = self.salary.text()
        #print("salary=",salary)
        xl = self.xl.currentText()

        # 当前文本框学历值为本科或研究生
        if xl == '本科' or xl == '研究生':
            school = self.school.text()
            graduate_time = self.graduate_time.text()
            major = self.major.text()
        else:
            school = "NULL"
            major = "NULL"
            graduate_time = "NULL"
        # print(school,graduate_time,major)



        # print(name+" "+sex+" "+birth+" "+tel+" "+address+" "+isMarried+" "+email+" "+identity+" ")
        if name == '' or tel == '' or address == '' or email == '' or identity == '' \
                or (xl == '本科' and school == '') or (xl == '本科' and major == '') or (xl == '研究生' and school == '') or (
                xl == '研究生' and major == '') or sex=='-请选择' or isMarried=='-请选择' \
                or department=='-请选择' or professional=='-请选择' or xl=='-请选择':
            reply = QMessageBox.information(self, "提示", "请正确填写信息!", QMessageBox.Yes)
        #elif re.match(r'[0-9a-zA-Z_]{0,19}@163.com',email):
        else:
            #邮箱不匹配
            if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',email):
                QMessageBox.information(self, "提示", "请填写正确邮箱！", QMessageBox.Yes)
                return

            #电话不匹配
            if len(str(tel)) != 11:
                QMessageBox.information(self, "提示", "请填写11位电话号码", QMessageBox.Yes)
                return

            #身份证号不匹配
            if len(str(identity)) != 14:
                QMessageBox.information(self, "提示", "请填写14位身份证号码", QMessageBox.Yes)
                return

            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:
                #获取下一个sno
                sql = "select max(convert(s_no,signed)) from staff"
                cursor.execute(sql)
                result = cursor.fetchone()
                maxsno = result[0]
                if maxsno == None:
                    newsno = 1
                else:
                    newsno = maxsno + 1

                needstr = ''
                if len(str(newsno)) < 6:
                    need = 6 - len(str(newsno))
                    print(need)
                    for i in range(need):
                        needstr += '0'
                newsno = needstr + str(newsno)

                #获取下一个pno
                sql = "select max(convert(p_no,signed)) from personnel"
                cursor.execute(sql)
                result = cursor.fetchone()
                maxpno = result[0]
                print('1',maxpno)
                if maxpno == None:
                    newpno = 1
                else:
                    newpno = maxpno + 1

                '''
                needstr = ''
                if len(str(newpno)) < 6:
                    need = 6 - len(str(newpno))
                    print(need)
                    for i in range(need):
                        needstr += '0'
                newpno = needstr + str(newpno)
               '''

                print("newpno",newpno)
                sql = "insert into staff (s_no,s_name,s_sex,s_birth,s_address,is_married,s_email,s_num,s_id) \
                                  values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                      (newsno, name, sex, birth, address, isMarried, email, tel, identity)
                #print(sql)
                cursor.execute(sql)


                sql = "select p_no from professional where p_name='%s'" % (professional)
                cursor.execute(sql)
                result = cursor.fetchone()
                p_no = result[0]

                sql = "select d_no from department where d_name='%s'" % (department)
                cursor.execute(sql)
                result = cursor.fetchone()
                d_no = result[0]
                print("newsno",newsno)
                #print(d_no,p_no)
                #print(entry_time)

                sql = "insert into sp values ( '%s','%s','%s','%s') "% (newsno,p_no,d_no,entry_time)
                cursor.execute(sql)


                sql = "insert into current_salary values( '%s','%s','%s','%s')" % (newsno,salary,'0','0')
                cursor.execute(sql)

                nowtime =  time.strftime("%Y-%m-%d",time.localtime())
                print(nowtime)
                #插入personnel
                sql = "insert into personnel values ('%s','%s','%s','%s','%s','%s','%s')"%(newpno,newsno,'无',department,'无',professional,nowtime)
                #print(sql)
                cursor.execute(sql)

                if xl == '本科' or xl == '研究生':
                    sql = "insert into education values( '%s','%s','%s','%s','%s')" % (newsno,xl, major, school, graduate_time)
                    cursor.execute(sql)
                else:
                    sql = "insert into education values('%s','%s',NULL,NULL,NULL) " % (newsno,xl)
                    cursor.execute(sql)

                QMessageBox.information(self, "提示", "添加成功!", QMessageBox.Yes)
                db.commit()

            except Exception as e:
                print(e)
                print("error1")


    def clearAll(self):
        self.name.clear()
        self.address.clear()
        self.tel.clear()
        self.email.clear()
        self.identity.clear()
        self.major.clear()
        self.school.clear()
        self.sex.setCurrentText("-请选择")
        self.isMarried.setCurrentText("-请选择")
        self.professional.setCurrentText("-请选择")
        self.department.setCurrentText("-请选择")
        self.xl.setCurrentText("-请选择")
        self.birth.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.graduate_time.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.entry_time.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.salary.clear()
    def showDetail(self):
        #print(self)

        xl = self.xl.currentText()
        #print(xl)

        if xl == '本科' or xl == '研究生':
            self.school.show()
            self.label_school.show()
            self.graduate_time.show()
            self.label_time.show()
            self.label_major.show()
            self.major.show()

            self.qingkong.setGeometry(QtCore.QRect(510, 450, 75, 23))
            self.add.setGeometry(QtCore.QRect(310, 450, 75, 23))



        else:
            self.school.hide()
            self.label_school.hide()
            self.graduate_time.hide()
            self.label_time.hide()
            self.label_major.hide()
            self.major.hide()
            self.qingkong.setGeometry(QtCore.QRect(510, 420, 75, 23))
            self.add.setGeometry(QtCore.QRect(310, 420, 75, 23))
#删除员工信息
class delete_staff(QtWidgets.QWidget,Ui_delete_staff):
    def __init__(self):
        super(delete_staff, self).__init__()
        self.setupUi(self)
    #点击删除按钮
    def btnclicked(self,btn):
        reply = QMessageBox.information(self,"提示","你是否真的要删除该员工的所有信息?",QMessageBox.Yes | QMessageBox.No)
        #print(reply)
        if reply == QMessageBox.Yes:
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            x = btn.frameGeometry().x()
            y = btn.frameGeometry().y()
            index = self.tableWidget.indexAt(QPoint(x, y))
            row = index.row()
            #row = self.tableWidget.currentRow()
            #print(row)
            sno = self.tableWidget.item(row, 0).text()  # 获取工号
            print("x",sno)

            try:
                sql="select count(*) from department where s_no='%s'"%(sno)
                cursor.execute(sql)
                result = cursor.fetchone()
                count=result[0]
                if count==0:


                    #print(status)
                    sql = "delete from sp where s_no='%s'"%(sno)
                    cursor.execute(sql)

                    sql = "delete from current_salary where s_no='%s'"%(sno)
                    cursor.execute(sql)

                    sql = "delete from education where s_no='%s'"%(sno)
                    cursor.execute(sql)

                    #print("zz")
                    sql = "delete from staff where s_no='%s'" % (sno)

                    cursor.execute(sql)
                    db.commit()
                    self.tableWidget.removeRow(row)
                else :
                    QMessageBox.information(self,"提示","该员工担任部门经理一职！请先进行人事调动！",QMessageBox.Yes)
            except Exception as e:
                print("error")
                print(e)

#查找员工
class find_staff(QtWidgets.QWidget,Ui_find_staff):
    def __init__(self):
        super(find_staff, self).__init__()
        self.setupUi(self)
    #查看详情按钮
    def btnclicked(self,btn):
        x = btn.frameGeometry().x()
        y = btn.frameGeometry().y()
        index = self.tableWidget.indexAt(QPoint(x,y))
        row = index.row()


        sno = self.tableWidget.item(row, 0).text()  # 获取工号

        for singer_obj in self.parent().children():
            #print(singer_obj.objectName)
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj

        # print(grid)
        content = self.parent()
        for singer_obj in content.children():
            #print(singer_obj)
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj, QtWidgets.QGridLayout) == False):
                singer_obj.hide()

        content.staff_detail_page = staff_detail()
        grid.addWidget(content.staff_detail_page)

        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()

        try:
            sql = "select * from staff where s_no='%s'"%(sno)
            cursor.execute(sql)
            result = cursor.fetchone()
            #print(result)
            sno = result[0]
            sname = result[1]
            sex = result[2]
            birth = result[3]
            identity = result[4]
            tel = result[5]
            email = result[6]
            isMarried = result[7]
            address = result[8]
           # print(birth)
            content.staff_detail_page.no.setText(str(sno))
            content.staff_detail_page.name.setText(sname)
            content.staff_detail_page.sex.setText(sex)
            content.staff_detail_page.isMarried.setText(isMarried)
            content.staff_detail_page.address.setText(address)
            content.staff_detail_page.birth.setText(str(birth))
            content.staff_detail_page.tel.setText(tel)
            content.staff_detail_page.email.setText(email)
            content.staff_detail_page.identity.setText(identity)

            sql = "select p_name,d_name,year(now())-year(entry_time) as workingtime from sp,professional,department where sp.d_no = department.d_no and sp.p_no = professional.p_no and sp.s_no='%s'"%(sno)
            cursor.execute(sql)
            result = cursor.fetchone()
            pname = result[0]
            dname = result[1]
            workingtime = result[2]
            content.staff_detail_page.department.setText(dname)
            content.staff_detail_page.professional.setText(pname)
            content.staff_detail_page.workingtime.setText(str(workingtime)+"年")
            sql = "select xl,major,school,graduate_date from education where s_no='%s'"%(sno)
            cursor.execute(sql)
            result = cursor.fetchone()
            xl = result[0]
            content.staff_detail_page.education.setText(xl)
            if xl == '本科' or xl == '研究生':
                content.staff_detail_page.label_school.show()
                content.staff_detail_page.label_major.show()
                content.staff_detail_page.label_time.show()
                content.staff_detail_page.school.show()
                content.staff_detail_page.time.show()
                content.staff_detail_page.major.show()
                major = result[1]
                school = result[2]
                time = result[3]
                print(time)
                content.staff_detail_page.major.setText(major)
                content.staff_detail_page.school.setText(school)
                content.staff_detail_page.time.setText(str(time))

        except:
            print("error")

    #显示全部员工
    def showall(self):
        if self.searchBox.text()=='':
            # 打开数据库
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            row = self.tableWidget.rowCount()
            i = row
            while i > 0:
                self.tableWidget.removeRow(i)
                i = i - 1
            try:
                cursor.execute("select s_no,s_name from staff")
                results = cursor.fetchall()
                # print(results)
                obj={}
                for row in results:
                    sno = row[0]
                    sname = row[1]

                    oldrow = self.tableWidget.rowCount()
                    self.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(sno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 1, item)

                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                    obj[strbtn].setText("详细信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")

                    self.one = partial(self.btnclicked, obj[strbtn])
                    # print(btn.objectName())
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.tableWidget.setCellWidget(oldrow, 2, obj[strbtn])
                    obj[strbtn].clicked.connect(self.one)
            except:
                print("error")

            #print("为空")
    #查找员工按钮
    def search(self):
        enter_con = self.searchBox.text()
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            sql = "select s_no,s_name from  staff where s_no = '%s' or s_name = '%s'"%(enter_con,enter_con)
            cursor.execute(sql)
            results = cursor.fetchall()

            if(len(results)==0):
                reply = QMessageBox.information(self,"tip","查无此人!",QMessageBox.Yes)
            else:
                row = self.tableWidget.rowCount()

                i=row
                while i>0:
                    self.tableWidget.removeRow(i)
                    i=i-1


                obj={}
                for row in results:
                    sno = row[0]
                    sname = row[1]

                    oldrow = self.tableWidget.rowCount()
                    self.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(sno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(sname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 1, item)

                    '''
                    btn = QtWidgets.QPushButton()
                    btn.setText("详细信息")
                    btn.setStyleSheet("text-decoration: underline")
                    btn.clicked.connect(self.btnclicked)
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                    self.tableWidget.setCellWidget(oldrow, 2, btn)
                   '''
                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                    obj[strbtn].setText("详细信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")

                    self.one = partial(self.btnclicked, obj[strbtn])
                    # print(btn.objectName())
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.tableWidget.setCellWidget(oldrow, 2, obj[strbtn])
                    obj[strbtn].clicked.connect(self.one)
        except:
            print("error")

#修改页面显示员工信息
class alter_display_staff(QtWidgets.QWidget,Ui_alter_display_staff):
    def __init__(self):
        super(alter_display_staff, self).__init__()
        self.setupUi(self)
    #查看详情按钮
    def btnclicked(self,btn):
        x = btn.frameGeometry().x()
        y = btn.frameGeometry().y()
        index = self.tableWidget.indexAt(QPoint(x, y))
        row = index.row()
        #row = self.tableWidget.currentRow()
        print(row)
        sno = self.tableWidget.item(row,0).text()#获取工号

        for singer_obj in self.parent().children():
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj

        #print(grid)
        content = self.parent()
        for singer_obj in content.children():
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False):
                singer_obj.hide()

        content.alter_staff_page = alter_staff()

        grid.addWidget(content.alter_staff_page)

        # 打开数据库
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            #读取基本信息
            cursor.execute(" select * from staff where s_no='%s'"%(sno))
            result = cursor.fetchone()
            print(result)

            sno = result[0]
            sname = result[1]
            sex= result[2]
            birth = result[3]
            identity = result[4]
            tel = result[5]
            email = result[6]
            isMarried = result[7]
            address = result[8]




            #读取学历信息
            cursor.execute(" select xl from education where s_no='%s'"%(sno))
            result = cursor.fetchone()
            xl = result[0]
            print(result)

            #读取职位部门信息
            cursor.execute("select p_name,d_name,entry_time from department,professional,sp where department.d_no = sp.d_no and professional.p_no = sp.p_no and sp.s_no='%s'"%(sno))
            result = cursor.fetchone()
            pname = result[0]
            dname = result[1]
            entry_time = result[2]
            print(result)

            #读取薪资信息
            print(sno)
            cursor.execute("select salary from current_salary where s_no='%s'"%(sno))
            result = cursor.fetchone()
            salary = result[0]
            content.alter_staff_page.salary.setProperty("value", salary)
            #print(salary)

            content.alter_staff_page.professional.setCurrentText(pname)
            content.alter_staff_page.department.setCurrentText(dname)
            content.alter_staff_page.entry_time.setDate(entry_time)

            content.alter_staff_page.no.setText(str(sno))
            content.alter_staff_page.name.setText(sname)
            content.alter_staff_page.sex.setCurrentText(sex)
            content.alter_staff_page.birth.setDate(QtCore.QDate(birth))
            content.alter_staff_page.address.setText(address)
            content.alter_staff_page.tel.setText(tel)
            content.alter_staff_page.isMarried.setCurrentText(isMarried)
            content.alter_staff_page.identity.setText(identity)
            content.alter_staff_page.email.setText(email)
            content.alter_staff_page.xl.setCurrentText(xl)

        except:
            print("error")

#修改员工信息
class alter_staff(QtWidgets.QWidget,Ui_alter_staff):
    def __init__(self):
        super(alter_staff, self).__init__()
        self.setupUi(self)
        self.label_school.hide()
        self.school.hide()
        self.label_time.hide()
        self.graduate_time.hide()
        self.label_major.hide()
        self.major.hide()

        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            sql = "select d_name from department"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                dname = row[0]
                self.department.addItem(dname)

            sql = "select p_name from professional"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                pname = row[0]
                self.professional.addItem(pname)
        except:
            print("error")
    #返回按钮
    def goback(self):
        for singer_obj in self.parent().children():
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj

        content = self.parent()
        for singer_obj in content.children():
            # print(singer_obj.objectName())
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,
                                                                                 QtWidgets.QGridLayout) == False):
                grid.removeWidget(singer_obj)
                singer_obj.deleteLater()
                sip.delete(singer_obj)
        self.alter_display_staff_page = alter_display_staff()
        grid.addWidget(self.alter_display_staff_page)

        # 打开数据库
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute(
                " select staff.s_no,staff.s_name,department.d_name from sp,staff,department where staff.s_no=sp.s_no and department.d_no=sp.d_no order by convert (staff.s_no,signed)")
            results = cursor.fetchall()
            # print(results)
            obj={}
            for row in results:
                sno = row[0]
                sname = row[1]
                dname = row[2]

                oldrow = self.alter_display_staff_page.tableWidget.rowCount()

                self.alter_display_staff_page.tableWidget.setRowCount(oldrow + 1)
                item = QTableWidgetItem(str(sno))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.alter_display_staff_page.tableWidget.setItem(oldrow, 0, item)

                item = QTableWidgetItem(sname)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.alter_display_staff_page.tableWidget.setItem(oldrow, 1, item)

                item = QTableWidgetItem(dname)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.alter_display_staff_page.tableWidget.setItem(oldrow, 2, item)

                strbtn = 'btn' + str(oldrow)
                obj[strbtn] = QtWidgets.QPushButton()

                obj[strbtn].setText("修改信息")
                obj[strbtn].setStyleSheet("text-decoration: underline")
                self.alter_display_staff_page.one = partial(self.alter_display_staff_page.btnclicked, obj[strbtn])
                obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                self.alter_display_staff_page.tableWidget.setCellWidget(oldrow, 3, obj[strbtn])
                obj[strbtn].clicked.connect(self.alter_display_staff_page.one)
                '''
                btn = QtWidgets.QPushButton()
                btn.setText("修改信息")
                btn.setStyleSheet("text-decoration: underline")
                btn.clicked.connect(self.alter_display_staff_page.btnclicked)
                btn.setCursor(QCursor(Qt.PointingHandCursor))
                self.alter_display_staff_page.tableWidget.setCellWidget(oldrow, 3, btn)
                '''
            # btn.click
        except Exception as e:
            print("error")

    #显示员工详细信息
    def showDetail(self):
        sno = self.no.text()
        print("sno=",sno)
        xl = self.xl.currentText()

        if xl == '本科' or xl == '研究生':
            self.school.show()
            self.label_school.show()
            self.graduate_time.show()
            self.label_time.show()
            self.label_major.show()
            self.major.show()
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:
                sql = "select major,school,graduate_date from education where s_no = '%s'"%(sno)
                cursor.execute(sql)
                result = cursor.fetchone()
               # print("ad",result)
                major = result[0]
                school = result[1]
                graduate_time = result[2]
                if major=='NULL':
                    #print("专业为空!")
                    self.major.setText("")
                if school=='NULL':
                    self.school.setText("")
                if graduate_time=='NULL':
                    self.graduate_time.setDate(QtCore.QDate(2018, 1, 1))
                if major!="NULL" and school!="NULL" and graduate_time!="NULL":
                    self.major.setText(major)
                    self.school.setText(school)
                    self.graduate_time.setDate(graduate_time)
            except:
                print("error")

            self.huifu.setGeometry(QtCore.QRect(500, 470, 75, 23))
            self.save.setGeometry(QtCore.QRect(300, 470, 75, 23))
        else:
            self.school.hide()
            self.label_school.hide()
            self.graduate_time.hide()
            self.label_time.hide()
            self.label_major.hide()
            self.major.hide()
            self.save.setGeometry(QtCore.QRect(300, 430, 75, 23))
            self.huifu.setGeometry(QtCore.QRect(500, 430, 75, 23))
    #保存按钮
    def saveInfo(self):
        sno = self.no.text()
        name =self.name.text()
        sex = self.sex.currentText()
        birth = self.birth.text()
        tel = self.tel.text()
        address = self.address.text()
        isMarried = self.isMarried.currentText()
        email = self.email.text()
        identity = self.identity.text()
        department = self.department.currentText()
        professional = self.professional.currentText()
        entry_time = self.entry_time.text()
        salary = self.salary.text()
        xl = self.xl.currentText()
        #当前文本框学历值为本科或研究生
        if xl=='本科' or xl=='研究生':
            school = self.school.text()
            graduate_time = self.graduate_time.text()
            major = self.major.text()
        else:
            school = "NULL"
            major = "NULL"
            graduate_time="NULL"

        if name == '' or tel == '' or address == '' or email == '' or identity == ''\
            or (xl=='本科' and school=='') or (xl=='本科' and major=='') or(xl=='研究生' and school=='') or(xl=='研究生' and major==''):
            reply = QMessageBox.information(self, "提示", "请正确填写信息!", QMessageBox.Yes)
        else:
            # 邮箱不匹配
            if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
                QMessageBox.information(self, "提示", "请填写正确邮箱！", QMessageBox.Yes)
                return

            # 电话不匹配
            if len(str(tel)) != 11:
                QMessageBox.information(self, "提示", "请填写11位电话号码", QMessageBox.Yes)
                return

            # 身份证号不匹配
            if len(str(identity)) != 14:
                QMessageBox.information(self, "提示", "请填写14位身份证号码", QMessageBox.Yes)
                return

            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:

                sql = "update staff set s_name='%s',s_sex='%s',s_birth='%s',s_address='%s',is_married='%s',s_email='%s',s_num='%s',s_id='%s' where s_no = '%s'" % (name, sex, birth, address, isMarried, email, tel, identity,sno)
                cursor.execute(sql)
                sql = "select p_no from professional where p_name='%s'"%(professional)
                s=cursor.execute(sql)
                result=cursor.fetchone()
                p_no = result[0]


                sql = "select d_no from department where d_name='%s'"%(department)
                cursor.execute(sql)
                result=cursor.fetchone()
                d_no = result[0]


                sql = "update sp set d_no = '%s',p_no='%s',entry_time='%s' where s_no='%s'" %(d_no,p_no,entry_time,sno)
                cursor.execute(sql)

                sql = "update current_salary set salary='%s' where s_no='%s'"%(salary,sno)
                cursor.execute(sql)
                #print("1",graduate_time)
                if xl=='本科' or xl=='研究生':
                    sql ="update education set xl='%s',major ='%s',school='%s',graduate_date='%s' where s_no='%s'"%(xl,major,school,graduate_time,sno)
                    cursor.execute(sql)
                else:
                    sql = "update education set xl='%s',major =NULL,school=NULL,graduate_date=NULL where s_no='%s'" % (xl, sno)
                    cursor.execute(sql)
                QMessageBox.information(self,"提示","保存成功!",QMessageBox.Yes)
                db.commit()

            except:
                print("error")
    #恢复按钮
    def restore(self):
        sno = self.no.text()
        # 打开数据库
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute(" select * from staff where s_no='%s'" % (sno))
            result = cursor.fetchone()
            sname = result[1]
            sex = result[2]
            birth = result[3]
            address = result[4]
            isMarried = result[5]
            email = result[6]
            tel = result[7]
            identity = result[8]

            # 读取学历信息
            cursor.execute(" select xl,school,major,graduate_date from education where s_no='%s'" % (sno))
            result = cursor.fetchone()
            xl = result[0]
            self.xl.setCurrentText(xl)
            if xl=='本科' or xl=='研究生':
                school = result[1]
                major = result[2]
                graduate_date = result[3]
                self.school.setText(school)
                self.major.setText(major)
                self.graduate_time.setDate(QtCore.QDate(birth))

            # 读取职位部门信息
            cursor.execute( "select p_name,d_name,entry_time from department,professional,sp where department.d_no = sp.d_no and professional.p_no = sp.p_no and sp.s_no='%s'" % (sno))
            result = cursor.fetchone()
            pname = result[0]
            dname = result[1]
            entry_time = result[2]
            # 读取薪资信息
            cursor.execute("select salary from salary where s_no='%s'" % (sno))
            result = cursor.fetchone()
            salary = result[0]
            self.salary.setProperty("value", salary)

            self.professional.setCurrentText(pname)
            self.department.setCurrentText(dname)
            self.entry_time.setDate(entry_time)

            self.name.setText(sname)
            self.sex.setCurrentText(sex)
            self.birth.setDate(QtCore.QDate(birth))
            self.address.setText(address)
            self.tel.setText(tel)
            self.isMarried.setCurrentText(isMarried)
            self.identity.setText(identity)
            self.email.setText(email)
        except:
            print("error")

#员工详情信息
class staff_detail(QtWidgets.QWidget,Ui_staff_detail):
    def __init__(self):
        super(staff_detail, self).__init__()
        self.setupUi(self)
        self.label_time.hide()
        self.label_major.hide()
        self.label_school.hide()
        self.time.hide()
        self.major.hide()
        self.school.hide()
    #返回按钮
    def goback(self):
        content = self.parent()
        for singer_obj in content.children():
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,                                                                           QtWidgets.QGridLayout) == False):
                if singer_obj.objectName() == 'staff_detail':
                    singer_obj.hide()
                elif singer_obj.objectName() == 'find_staff':
                    singer_obj.show()
                elif singer_obj.objectName() == 'find_dept':
                    singer_obj.hide()
                elif singer_obj.objectName() == 'dept_detail':
                    singer_obj.show()


#修改部门信息-基本信息显示
class alter_display_dept(QtWidgets.QWidget,Ui_alter_display_dept):
    def __init__(self):
        super(alter_display_dept, self).__init__()
        self.setupUi(self)

    #查看详情按钮
    def btnclicked(self,btn):
        x = btn.frameGeometry().x()
        y = btn.frameGeometry().y()
        index = self.tableWidget.indexAt(QPoint(x, y))
        row = index.row()
        dno = self.tableWidget.item(row, 0).text()  # 获取部门编号


        for singer_obj in self.parent().children():
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj
        content = self.parent()
        for singer_obj in content.children():
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False):
                singer_obj.hide()

        content.alter_dept_page = alter_dept()

        grid.addWidget(content.alter_dept_page)
        content.alter_dept_page.no.setText(dno)
        #content.alter_dept_page.manager.addItem("-请选择")
        # 打开数据库
        content.alter_dept_page.manager.addItem("-暂无")
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute(" select s_no,s_name from staff")
            results = cursor.fetchall()
            #print(results)
            for row in results:
                sno = row[0]
                sname = row[1]
                employee = sno + "-" + sname
                content.alter_dept_page.manager.addItem(employee)
        except:
            print("error")


        # 显示原来信息
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute("select s_no from department where d_no='%s'"%(dno))
            result = cursor.fetchone()
            #print("hhhh",result)
            re = result[0]
            if re == None:
                cursor.execute("select d_name from department where d_no='%s'"%(dno))
                result = cursor.fetchone()
                dname = result[0]
                content.alter_dept_page.name.setText(dname)
                content.alter_dept_page.manager.setCurrentText("暂无")
            else:
                cursor.execute(" select d_no,d_name,staff.s_no,staff.s_name from department,staff where  staff.s_no=department.s_no and d_no='%s'" % (dno))
                result = cursor.fetchone()
                #print(result)

                dno = result[0]
                dname = result[1]
                sno = result[2]
                sname = result[3]
                print(dno,dname,sname,sno)
                strman = sno+'-'+sname
                print(strman)

                content.alter_dept_page.name.setText(dname)
                content.alter_dept_page.manager.setCurrentText(strman)
        except:
            print("error")

#增加部门
class add_dept(QtWidgets.QWidget,Ui_add_dept):
    def __init__(self):
        super(add_dept, self).__init__()
        self.setupUi(self)
        self.manager.addItem("-请选择")
        self.manager.addItem("-暂无")
        # 打开数据库
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute(" select s_no,s_name from staff")
            results = cursor.fetchall()
            #print(results)
            for row in results:
                sno=row[0]
                sname=row[1]
                employee = str(sno)+"-"+sname
                self.manager.addItem(employee)
        except:
            print("error")
    #添加按钮
    def addDept(self):
        name = self.name.text()
        snostr = self.manager.currentText()
        re = snostr.split('-')


        if name == '' or re[1]=='请选择':
            QMessageBox.information(self,"提示","请正确输入!",QMessageBox.Yes)
        else:
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()

            try:
                #-----------dno
                sql = "select max(convert(d_no,signed)) from department"
                cursor.execute(sql)
                result = cursor.fetchone()
                maxdno = result[0]

                if maxdno == None:
                    newdno = 1
                else:
                    newdno = int(maxdno) + 1

                needstr=''
                if len(str(newdno))<6:
                    need = 6-len(str(newdno))
                    print(need)
                    for i in range(need):
                        needstr +='0'
                newdno=needstr+str(newdno)

                #---------pno personnel
                #获取下一个pno
                sql = "select max(convert(p_no,signed)) from personnel"
                cursor.execute(sql)
                result = cursor.fetchone()
                maxpno = result[0]
                print('1',maxpno)
                if maxpno == None:
                    newpno = 1
                else:
                    newpno = maxpno + 1

                needstr = ''
                if len(str(newpno)) < 6:
                    need = 6 - len(str(newpno))
                    print(need)
                    for i in range(need):
                        needstr += '0'
                newpno = needstr + str(newpno)

                if re[1]=='暂无':
                    sql = "insert into department (d_no,d_name) values ('%s','%s')" % (newdno,name)
                    cursor.execute(sql)
                else:
                    sno=re[0]
                    sql = "select d_name,s_name from staff,department where department.s_no = staff.s_no and staff.s_no='%s'"%(sno)
                    cursor.execute(sql)
                    result = cursor.fetchone()

                    if result!=None:#如果已经是别的部门的经理
                        dname = result[0]
                        sname = result[1]
                        tip = sname+"已在"+dname+"任职,是否仍要重新任职？"
                        reply=QMessageBox.information(self,"提示",tip,QMessageBox.Yes|QMessageBox.No)
                        if reply == QMessageBox.Yes:


                            #-------------
                            sql = "select d_name,p_name from sp,department,professional where sp.s_no='%s' and sp.p_no=professional.p_no and sp.d_no=department.d_no"%(sno)
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            oldDname = result[0]
                            oldPname = result[1]
                            # 插入personnel
                            nowtime = time.strftime("%Y-%m-%d", time.localtime())
                            sql = "insert into personnel values ('%s','%s','%s','%s','%s','%s','%s')" % (newpno,sno, oldDname, name, oldPname, "经理", nowtime)
                            #print(sql)
                            cursor.execute(sql)

                            sql = "update department set s_no=NULL where s_no='%s'" % (sno)  # 先把原部门设置为暂无经理
                            cursor.execute(sql)
                            sql = "insert into department (d_no,d_name,s_no) values ('%s','%s','%s')" % (
                            newdno, name, sno)
                            cursor.execute(sql)
                            sql = "update sp set d_no = '%s' where s_no = '%s'" % (newdno, sno)  # 更新人事表
                            cursor.execute(sql)
                        else:return
                    else:
                        #print("执行")

                        # -------------
                        sql = "select d_name,p_name from sp,department,professional where sp.s_no='%s' and sp.p_no=professional.p_no and sp.d_no=department.d_no" % (
                            sno)
                        cursor.execute(sql)
                        result = cursor.fetchone()
                        print(result)
                        oldDname = result[0]
                        oldPname = result[1]
                        # 插入personnel
                        nowtime = time.strftime("%Y-%m-%d", time.localtime())
                        sql = "insert into personnel values ('%s','%s','%s','%s','%s','%s','%s')" % (
                        newpno, sno, oldDname, name, oldPname, "经理", nowtime)
                        # print(sql)

                        sql = "insert into department (d_no,d_name,s_no) values ('%s','%s','%s')" % (newdno, name, sno)
                        cursor.execute(sql)

                        sql = "update sp set d_no = '%s' where s_no = '%s'" % (newdno, sno)  # 更新人事表
                        cursor.execute(sql)

                        cursor.execute(sql)

                db.commit()
                self.name.clear()
                self.manager.setCurrentText("-请选择")
                QMessageBox.information(self, "提示", "添加成功!", QMessageBox.Yes)

            except Exception as e:
                print("error")
                print(e)
    #清空按钮
    def clearAll(self):
        self.name.clear()
        self.manager.setCurrentText("-请选择")
#修改部门信息
class alter_dept(QtWidgets.QWidget,Ui_alter_dept):
    def __init__(self):
        super(alter_dept, self).__init__()
        self.setupUi(self)
    #返回按钮
    def goback(self):
        for singer_obj in self.parent().children():
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj

        content = self.parent()
        for singer_obj in content.children():
            # print(singer_obj.objectName())
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False):
                grid.removeWidget(singer_obj)
                singer_obj.deleteLater()
                sip.delete(singer_obj)
        self.alter_display_dept_page = alter_display_dept()
        grid.addWidget(self.alter_display_dept_page)

        # 打开数据库
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute(
                " select d_no,d_name,s_no from department")
            results = cursor.fetchall()
            #print(results)
            obj={}
            for row in results:
                dno = row[0]
                dname = row[1]
                sno = row[2]
                #print(dno, dname, sno)

                if sno == None:
                    sname = '暂无'
                else:
                    cursor.execute("select s_name from staff where s_no='%s'" % (sno))
                    result = cursor.fetchone()
                    sname = result[0]
                #print(sname)

                oldrow = self.alter_display_dept_page.tableWidget.rowCount()

                self.alter_display_dept_page.tableWidget.setRowCount(oldrow + 1)
                item = QTableWidgetItem(str(dno))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.alter_display_dept_page.tableWidget.setItem(oldrow, 0, item)

                item = QTableWidgetItem(dname)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.alter_display_dept_page.tableWidget.setItem(oldrow, 1, item)

                item = QTableWidgetItem(sname)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.alter_display_dept_page.tableWidget.setItem(oldrow, 2, item)

                strbtn = 'btn' + str(oldrow)
                obj[strbtn] = QtWidgets.QPushButton()

                obj[strbtn].setText("修改信息")
                obj[strbtn].setStyleSheet("text-decoration: underline")

                self.alter_display_dept_page.one = partial(self.alter_display_dept_page.btnclicked, obj[strbtn])
                # print(btn.objectName())
                obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                self.alter_display_dept_page.tableWidget.setCellWidget(oldrow, 3, obj[strbtn])
                obj[strbtn].clicked.connect(self.alter_display_dept_page.one)
            # btn.click
        except:
            print("error")
    #保存按钮
    def saveInfo(self):
        dno = self.no.text()
        name = self.name.text()
        snostr = self.manager.currentText()
        re = snostr.split('-')
        #print("re=",re)
        if name == '' or re[1] == '请选择':
            QMessageBox.information(self, "提示", "请正确输入!", QMessageBox.Yes)
        else:
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:
                # ---------pno personnel
                # 获取下一个pno
                sql = "select max(convert(p_no,signed)) from personnel"
                cursor.execute(sql)
                result = cursor.fetchone()
                maxpno = result[0]
                print('1', maxpno)
                if maxpno == None:
                    newpno = 1
                    nextpno = 2
                else:
                    newpno = maxpno + 1
                    nextpno = maxpno + 2

                needstr1 = ''
                needstr2=''
                newpno = needstr1 + str(newpno)
                nextpno = needstr2 + str(nextpno)
                if len(str(newpno)) < 6:
                    need = 6 - len(str(newpno))
                    #print(need)
                    for i in range(need):
                        needstr1 += '0'
                if len(str(nextpno)) < 6:
                    need = 6 - len(str(nextpno))
                    #print(need)
                    for i in range(need):
                        needstr2 += '0'

                print('newpno=', newpno)
                print('nextpno=', nextpno)

                if re[1] == '暂无':
                    sql = "update department set s_no=NULL ,d_name='%s'" % (name)
                    cursor.execute(sql)
                    db.commit()
                else:
                    sno = re[0]
                   #print(sno)
                    sql = "select count(*) from department where s_no='%s'"%(sno)
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    count = result[0]
                    if count!=0:  # 如果已经是别的部门的经理
                        sql = "select d_name,s_name from staff,department where department.s_no = staff.s_no and staff.s_no='%s'" % (
                            sno)
                        cursor.execute(sql)
                        result = cursor.fetchone()
                        #print('vvv', result)
                        dname = result[0]
                        sname = result[1]
                        tip = sname + "已在" + dname + "任职,是否仍要重新任职？"
                        reply = QMessageBox.information(self, "提示", tip, QMessageBox.Yes | QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            sql = "update department set s_no=NULL where s_no='%s'" % (sno)  # 先把原部门设置为暂无经理
                            cursor.execute(sql)
                            sql = "update department set d_name='%s',s_no='%s' where d_no='%s'" % (name, sno, dno)
                            cursor.execute(sql)
                            sql = "update sp set d_no = '%s' where s_no = '%s'" % (dno, sno)  # 更新人事表
                            cursor.execute(sql)

                            db.commit()
                            QMessageBox.information(self, "提示", "更新成功!", QMessageBox.Yes)

                            '''
                            # -------------
                            #更改新经理personnel
                            sql = "select d_name,p_name from sp,department,professional where sp.s_no='%s' and sp.p_no=professional.p_no and sp.d_no=department.d_no" % (sno)
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            print('x',result)
                            oldDname = result[0]
                            oldPname = result[1]
                            # 插入personnel
                            nowtime = time.strftime("%Y-%m-%d", time.localtime())
                            sql = "insert into personnel values ('%s','%s','%s','%s','%s','%s','%s')" % (newpno, sno, oldDname, name, oldPname, "经理", nowtime)
                            cursor.execute(sql)
                            print(newpno)

                            # --------更改旧经理personnel
                            sql = "select s_no,d_name from department where d_no='%s'" % (dno)
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            oldsno = result[0]
                            if oldsno==None:#之前有经理
                                oldDname = result[1]
                                print(oldsno,oldDname)
                                sql = "insert into personnel values ('%s','%s','%s','%s','%s','%s','%s')" % (nextpno, oldsno, oldDname, oldDname, "经理", "无", nowtime)
                                cursor.execute(sql)
                            '''
                        else:return
                    else:
                        '''
                        nowtime = time.strftime("%Y-%m-%d", time.localtime())
                        # -------------
                        # 更改新经理personnel
                        sql = "select d_name,p_name from sp,department,professional where sp.s_no='%s' and sp.p_no=professional.p_no and sp.d_no=department.d_no" % (
                            sno)
                        cursor.execute(sql)
                        result = cursor.fetchone()
                        print('x', result)
                        oldDname = result[0]
                        oldPname = result[1]
                        # 插入personnel
                        sql = "insert into personnel values ('%s','%s','%s','%s','%s','%s','%s')" % (
                            newpno, sno, oldDname, name, oldPname, "经理", nowtime)
                        cursor.execute(sql)
                        #--------更改旧经理personnel
                        sql = "select s_no,d_name from department where d_no='%s'" % (dno)
                        cursor.execute(sql)
                        result = cursor.fetchone()
                        oldsno = result[0]
                        oldDname = result[1]
                        sql = "insert into personnel values ('%s','%s','%s','%s','%s','%s','%s')" % (
                            nextpno, oldsno, name,name, "经理", "无", nowtime)
                        cursor.execute(sql)
                    '''
                        # print("dname=")
                        sql = "update department set d_name='%s',s_no='%s' where d_no='%s'" % (name, sno, dno)
                        cursor.execute(sql)


                        sql = "update sp set d_no = '%s' where s_no = '%s'" % (dno, sno)  # 更新人事表
                        cursor.execute(sql)
                        # sql = ""
                        db.commit()
                        QMessageBox.information(self, "提示", "更新成功!", QMessageBox.Yes)

            except Exception as e:
                print("error")
                print(e)
    #恢复按钮
    def restore(self):
        # 打开数据库
        dno = self.no.text()
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute("select d_name,s_no from department where d_no='%s'"%(dno))
            result = cursor.fetchone()
            #print("x",result)
            dname = result[0]
            sno = result[1]
            if sno==None:
                self.manager.setCurrentText("-暂无")
                self.name.setText(dname)
            else:
                cursor.execute(
                    " select d_no,d_name,staff.s_no,staff.s_name from department,staff where  staff.s_no=department.s_no and d_no='%s'" % (
                        dno))
                result = cursor.fetchone()
                # print(result)

                dno = result[0]
                dname = result[1]
                sno = result[2]
                sname = result[3]
                #print(dno, dname, sname, sno)
                strman = sno + '-' + sname
                self.name.setText(dname)
                self.manager.setCurrentText(strman)
        except:
            print("error")

#删除部门信息
class delete_dept(QtWidgets.QWidget,Ui_delete_dept):
    def __init__(self):
        super(delete_dept, self).__init__()
        self.setupUi(self)
    #删除按钮
    def btnclicked(self,btn):
        reply = QMessageBox.information(self,"提示","您是否真的要删除该部门?",QMessageBox.Yes | QMessageBox.No)
        #print(reply)
        if reply == QMessageBox.Yes:
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()

            x = btn.frameGeometry().x()
            y = btn.frameGeometry().y()
            index = self.tableWidget.indexAt(QPoint(x, y))
            row = index.row()
            dno = self.tableWidget.item(row, 0).text()

            try:
                sql="select count(*) from sp where d_no='%s'"%(dno)
                cursor.execute(sql)
                result = cursor.fetchone()
                count = result[0]
                if count==0:
                    self.tableWidget.removeRow(row)
                    sql  = "delete from department where d_no='%s'"%(dno)
                    cursor.execute(sql)
                    db.commit()
                else:
                    QMessageBox.warning(self,"警告","该部门中仍有员工，请先进行人员调动!",QMessageBox.Yes)
            except:
                print("error")

#查找部门信息
class find_dept(QtWidgets.QWidget,Ui_find_dept):
    def __init__(self):
        super(find_dept, self).__init__()
        self.setupUi(self)
    #部门详细信息按钮
    def btnclicked(self,btn):
        x = btn.frameGeometry().x()
        y = btn.frameGeometry().y()
        index = self.tableWidget.indexAt(QPoint(x, y))
        row = index.row()
        #row = self.tableWidget.currentRow()
        dno = self.tableWidget.item(row, 0).text()  # 获取部门编号

        #print(dno)

        for singer_obj in self.parent().children():
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj
        content = self.parent()

        for singer_obj in content.children():

            if isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False and isinstance(singer_obj,find_dept) == False:
                grid.removeWidget(singer_obj)
                singer_obj.deleteLater()
                sip.delete(singer_obj)
        for singer_obj in content.children():
        #    print(singer_obj.objectName())
            if isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False:
                singer_obj.hide()

        content.dept_detail_page = dept_detail()

        grid.addWidget(content.dept_detail_page)

        content.dept_detail_page.no.setText(dno)

        #test
        #for singer_obj in content.dept_detail_page.children():
        #    print(singer_obj.objectName())


        # 打开数据库
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            #该部门信息

            cursor.execute("select s_no from department where d_no='%s'"%(dno))
            result=cursor.fetchone()
            sno = result[0]
            print(sno)
            if sno==None:
                cursor.execute("select d_name from department where d_no='%s'"%(dno))
                result = cursor.fetchone()
                dname = result[0]
                content.dept_detail_page.name.setText(dname)
                content.dept_detail_page.manager.setText("暂无")
            else:
                cursor.execute("select d_name,staff.s_no,s_name from staff,department where staff.s_no = department.s_no and d_no='%s'"%(dno))
                result = cursor.fetchone()
                dname = result[0]
                sno = result[1]
                #print(sno)
                manager = result[2]
                snoman = sno+" - "+manager
                content.dept_detail_page.name.setText(dname)
                content.dept_detail_page.manager.setText( snoman)
            cursor.execute("select count(*) from sp where sp.d_no ='%s'"%(dno))
            result = cursor.fetchone()
            num = result[0]
            #print(num)
            content.dept_detail_page.num.setText(str(num)+"人")
            #该部门员工员工信息
            cursor.execute( "select staff.s_no,staff.s_name from sp,staff where sp.s_no = staff.s_no and d_no='%s'  order by convert (staff.s_no,signed)" % (dno))
            results = cursor.fetchall()
            print(results)

            obj={}
            for row in results:
                sno = row[0]
                sname = row[1]
                #print(sname)

                oldrow = content.dept_detail_page.tableWidget.rowCount()

                content.dept_detail_page.tableWidget.setRowCount(oldrow + 1)
                item = QTableWidgetItem(str(sno))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                content.dept_detail_page.tableWidget.setItem(oldrow, 0, item)

                item = QTableWidgetItem(sname)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                content.dept_detail_page.tableWidget.setItem(oldrow, 1, item)

                '''
                btn = QtWidgets.QPushButton()
                btn.setText("详细信息")
                btn.setStyleSheet("text-decoration: underline")
                btn.setCursor(QCursor(Qt.PointingHandCursor))
                #btn.clicked.connect(content.dept_detail_page.btnclicked)
                content.dept_detail_page.tableWidget.setCellWidget(oldrow, 2, btn)
                '''
                strbtn = 'btn' + str(oldrow)
                obj[strbtn] = QtWidgets.QPushButton()
                obj[strbtn].setText("详细信息")
                obj[strbtn].setStyleSheet("text-decoration: underline")
                content.dept_detail_page.one = partial(content.dept_detail_page.btnclicked, obj[strbtn])
                obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))

                content.dept_detail_page.tableWidget.setCellWidget(oldrow, 2, obj[strbtn])
               
                obj[strbtn].clicked.connect(content.dept_detail_page.one)

        except:
            print("error")
    #显示全部按钮
    def showall(self):
        if self.searchBox.text()=='':
            # 打开数据库
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            row = self.tableWidget.rowCount()
            i = row
            while i > 0:
                self.tableWidget.removeRow(i)
                i = i - 1
            try:
                cursor.execute("select d_no,d_name from department")
                results = cursor.fetchall()
                # print(results)
                obj={}
                for row in results:
                    dno = row[0]
                    dname = row[1]

                    oldrow = self.tableWidget.rowCount()
                    self.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(dno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(dname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 1, item)
                    '''
                    btn = QtWidgets.QPushButton()
                    btn.setText("详细信息")
                    btn.setStyleSheet("text-decoration: underline")
                    btn.clicked.connect(self.btnclicked)
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                    self.tableWidget.setCellWidget(oldrow, 2, btn)
                    '''
                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                    obj[strbtn].setText("详细信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")
                    self.one = partial(self.btnclicked, obj[strbtn])
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.tableWidget.setCellWidget(oldrow, 2, obj[strbtn])
                    obj[strbtn].clicked.connect(self.one)

            except:
                print("error")
    #查找按钮
    def search(self):
        enter_con = self.searchBox.text()
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            sql = "select d_no,d_name from  department where d_no = '%s' or d_name = '%s'" % (enter_con, enter_con)
            cursor.execute(sql)
            results = cursor.fetchall()

            if (len(results) == 0):
                reply = QMessageBox.information(self, "提示", "该部门不存在！", QMessageBox.Yes)
            else:
                row = self.tableWidget.rowCount()

                i = row
                while i > 0:
                    self.tableWidget.removeRow(i)
                    i = i - 1
                obj={}
                for row in results:
                    dno = row[0]
                    dname = row[1]

                    oldrow = self.tableWidget.rowCount()
                    self.tableWidget.setRowCount(oldrow + 1)
                    item = QTableWidgetItem(str(dno))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 0, item)

                    item = QTableWidgetItem(dname)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(oldrow, 1, item)
                    '''
                    btn = QtWidgets.QPushButton()
                    btn.setText("详细信息")
                    btn.setStyleSheet("text-decoration: underline")
                    btn.clicked.connect(self.btnclicked)
                    btn.setCursor(QCursor(Qt.PointingHandCursor))
                    self.tableWidget.setCellWidget(oldrow, 2, btn)
                    '''
                    strbtn = 'btn' + str(oldrow)
                    obj[strbtn] = QtWidgets.QPushButton()

                    obj[strbtn].setText("详细信息")
                    obj[strbtn].setStyleSheet("text-decoration: underline")
                    self.one = partial(self.btnclicked, obj[strbtn])
                    obj[strbtn].setCursor(QCursor(Qt.PointingHandCursor))
                    self.tableWidget.setCellWidget(oldrow, 2, obj[strbtn])
                    obj[strbtn].clicked.connect(self.one)
        except:
            print("error")
#部门详细信息
class dept_detail(QtWidgets.QWidget,Ui_dept_detail):
    def __init__(self):
        super(dept_detail, self).__init__()
        self.setupUi(self)
    #返回按钮
    def goback(self):
        content = self.parent()
        for singer_obj in content.children():
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False):
                if singer_obj.objectName() == 'find_dept':
                    singer_obj.show()
                else:
                    singer_obj.hide()
    #查看详情按钮
    def btnclicked(self,btn):
        content = self.parent()
        for singer_obj in content.children():
            #print(singer_obj.objectName())
            if (isinstance(singer_obj, QtWidgets.QLabel) == False and isinstance(singer_obj,QtWidgets.QGridLayout) == False):
                    singer_obj.hide()

        x = btn.frameGeometry().x()
        y = btn.frameGeometry().y()
        index = self.tableWidget.indexAt(QPoint(x, y))
        row = index.row()
        sno = self.tableWidget.item(row, 0).text()  # 获取工号
        #print(sno)
        for singer_obj in self.parent().children():
            #print(singer_obj.objectName)
            if isinstance(singer_obj, QtWidgets.QGridLayout) == True:
                grid = singer_obj

        content.staff_detail_page = staff_detail()
        grid.addWidget(content.staff_detail_page)

        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()

        try:
            sql = "select * from staff where s_no='%s'"%(sno)
            cursor.execute(sql)
            result = cursor.fetchone()
            #print(result)
            sno = result[0]
            sname = result[1]
            sex = result[2]
            birth = result[3]
            address = result[4]
            isMarried = result[5]
            email = result[6]
            tel = result[7]
            identity = result[8]

            #print(birth)
            content.staff_detail_page.no.setText(str(sno))
            content.staff_detail_page.name.setText(sname)
            content.staff_detail_page.sex.setText(sex)
            content.staff_detail_page.isMarried.setText(isMarried)
            content.staff_detail_page.address.setText(address)
            content.staff_detail_page.birth.setText(str(birth))
            content.staff_detail_page.tel.setText(tel)
            content.staff_detail_page.email.setText(email)
            content.staff_detail_page.identity.setText(identity)

            sql = "select p_name,d_name,year(now())-year(entry_time) as workingtime from sp,professional,department where sp.d_no = department.d_no and sp.p_no = professional.p_no and sp.s_no='%s'"%(sno)
            cursor.execute(sql)
            result = cursor.fetchone()
            pname = result[0]
            dname = result[1]
            workingtime = result[2]
            content.staff_detail_page.department.setText(dname)
            content.staff_detail_page.professional.setText(pname)
            content.staff_detail_page.workingtime.setText(str(workingtime)+"年")
            sql = "select xl,major,school from education where s_no='%s'"%(sno)
            cursor.execute(sql)
            result = cursor.fetchone()
            xl = result[0]
            major = result[1]
            school = result[2]
            content.staff_detail_page.education.setText(xl)
            content.staff_detail_page.major.setText(major)
            content.staff_detail_page.school.setText(school)
        except:
            print("error")
#管理权限界面
class admin(QtWidgets.QWidget,Ui_admin):
    def __init__(self):
        super(admin, self).__init__()
        self.setupUi(self)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
    #产生右键触发菜单
    def generateMenu(self, pos):
        # print(pos)
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        menu = QMenu()
        #item1 = menu.addAction("添加管理员")
        #item2 = menu.addAction("删除管理员")
        item3 = menu.addAction("修改密码")
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        '''
        if action == item1:  # 添加
            self.add_admin_page = add_admin(self)
            self.add_admin_page.show()
        elif action == item2:  # 删除
            row = self.tableWidget.currentRow()
            sno = self.tableWidget.item(row, 0).text()  # 获取工号
            if sno == "1":
                print("执行")
                reply = QMessageBox.information(self, "提示", "该用户为超级管理员！无法删除！", QMessageBox.Yes )
            elif row!=0:
                reply = QMessageBox.information(self, "提示", "您是否确定要删除该管理员?", QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    db = pymysql.connect("localhost", "user", "123456", "personnel_man")
                    cursor = db.cursor()
                    try:
                        sql = "delete from admin_table where s_no = '%s'"%(sno)
                        cursor.execute(sql)
                        db.commit()
                        row = self.tableWidget.currentRow()
                        self.tableWidget.removeRow(row)
                    except:
                        print("error")
'''
        if action == item3:  # 修改
            row = self.tableWidget.currentRow()
            sno = self.tableWidget.item(row, 0).text()  # 获取工号

            self.alter_admin_page = alter_admin(self)
            self.alter_admin_page.show()
            self.alter_admin_page.sno.setText(sno)
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:
                sql = "select pwd from admin_table where s_no = '%s'" % (sno)
                cursor.execute(sql)
                result = cursor.fetchone()
                pwd = result[0]
                self.alter_admin_page.pwd.setText(pwd)
                #self.alter_profess_page.no.setText(pno)
                # print(result)
            except:
                print("error1")


        else:
            return
#添加管理员
class add_admin(QtWidgets.QWidget,Ui_add_admin):
    def __init__(self,professAdmin):
        super(add_admin,self).__init__()
        self.setupUi(self)
        self.profess_admin = professAdmin

        self.staff.addItem("-请选择")
        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            sql = "select s_no,s_name from staff"
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                sno = row[0]
                sname = row[1]
                staffstr = sno+'-'+sname
                self.staff.addItem(staffstr)
        except:
            print("error")
    #添加按钮
    def add(self):
        staffstr = self.staff.currentText()
        sta = staffstr.split('-')[1]
        pwd  = self.pwd.text()
        if sta == '请选择' or pwd=='':
            QMessageBox.information(self,"提示","请正确填写信息！",QMessageBox.Yes)
        else:
            sno = staffstr.split('-')[0]
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:
                sql = "select count(*) from admin_table where s_no='%s'" % (sno)
                cursor.execute(sql)
                result = cursor.fetchone()
                count= result[0]
                if count==0:#不是管理员
                    sql = "insert into admin_table values('%s','%s')" % (sno, pwd)
                    status = cursor.execute(sql)
                    db.commit()
                    if status == 1:
                        self.rewrite()
                    reply = QMessageBox.information(self, "提示", "添加成功！", QMessageBox.Yes)
                    if reply == QMessageBox.Yes:
                        self.close()
                else:#已经是管理员
                    QMessageBox.information(self,"提示","该员工已是管理员",QMessageBox.Yes)
                    self.staff.setCurrentText("-请选择")
                    self.pwd.clear()
            except:
                print("error")
    #重写表格
    def rewrite(self):

        professA = self.profess_admin
        rows = professA.tableWidget.rowCount()
        # print(rows)
        i = rows
        while i > 0:
            professA.tableWidget.removeRow(i)
            i = i - 1

        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute("select s_no,pwd from admin_table order by convert(s_no,signed)")
            results = cursor.fetchall()
            #print("hello", results)

            for row in results:
                sno = row[0]
                pwd = row[1]
                oldrow = professA.tableWidget.rowCount()
                print('oldrow=', oldrow)
                professA.tableWidget.setRowCount(oldrow + 1)
                item = QTableWidgetItem(sno)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 0, item)

                item = QTableWidgetItem(pwd)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 1, item)

        except:
            print("error")
#修改密码
class alter_admin(QtWidgets.QWidget,Ui_alter_admin):
    def __init__(self,professAdmin):
        super(alter_admin, self).__init__()
        self.setupUi(self)
        self.profess_admin = professAdmin
    #保存按钮
    def save(self):
        sno = self.sno.text()
        pwd = self.pwd.text()
        if pwd == '':
            QMessageBox.information(self, "提示", "请正确填写密码!", QMessageBox.Yes)

        else:
            db = pymysql.connect("localhost", "user", "123456", "personnel_man")
            cursor = db.cursor()
            try:
                print(pwd,sno)
                sql = "update admin_table set pwd='%s' where s_no='%s'"%(pwd,sno)
                status = cursor.execute(sql)
                db.commit()
                if status == 1:
                    self.rewirte()
                reply = QMessageBox.information(self, "提示", "保存成功！", QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    self.close()
            except:
                print("error2")
    #重写按钮
    def rewirte(self):
        professA = self.profess_admin
        rows = professA.tableWidget.rowCount()
        i = rows
        while i > 0:
            professA.tableWidget.removeRow(i)
            i = i - 1

        db = pymysql.connect("localhost", "user", "123456", "personnel_man")
        cursor = db.cursor()
        try:
            cursor.execute("select s_no,pwd from admin_table order by convert(s_no,signed)")
            results = cursor.fetchall()
            for row in results:
                sno = row[0]
                pwd = row[1]
                oldrow = professA.tableWidget.rowCount()
                #print('oldrow=', oldrow)
                professA.tableWidget.setRowCount(oldrow + 1)
                item = QTableWidgetItem(sno)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 0, item)

                item = QTableWidgetItem(pwd)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                professA.tableWidget.setItem(oldrow, 1, item)

        except:
            print("error")

#拼接
#薪资历史查询
class find_salary(salaryHistory):
    def __init__(self):
        super(find_salary, self).__init__()
        self.setupUi(self)

#薪资分配管理
class alter_salary(salaryNow):
    def __init__(self):
        super(alter_salary, self).__init__()
        self.setupUi(self)

#调动历史查询
class find_personal(personnel_history):
    def __init__(self):
        super(find_personal, self).__init__()
        self.setupUi(self)

#人员调动
class alter_personal(personnel_now):
    def __init__(self):
        super(alter_personal, self).__init__()
        self.setupUi(self)

#人员考核
class alter_check(checkChange):
    def __init__(self):
        super(alter_check, self).__init__()
        self.setupUi(self)

#考核历史查询
class find_check(checkHistory):
    def __init__(self):
        super(find_check, self).__init__()
        self.setupUi(self)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = login()
    login_window.show()
    sys.exit(app.exec_())