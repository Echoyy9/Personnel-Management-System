import  sys
import  pymysql
from PyQt5 import QtWidgets
from staff import Ui_MainWindow
import sip

class staffAdmin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(staffAdmin, self).__init__()
        self.setupUi(self)

    def test(self):
        self.tableWidget.hide()







if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_staffAdmin = staffAdmin()
    my_staffAdmin.show()
    #打开数据库
    '''
    db = pymysql.connect("localhost", "user", "123456", "personnel_man")
    cursor = db.cursor()
    try:
        cursor.execute("select * from department")
        results = cursor.fetchall()
        for row in results:
            dno = row[0]
            dname = row[1]
            sno = row[2]
            print(dname)
            my_staffAdmin.textBrowser.append("%8s\t%8s\t%8s" %(dno,dname,sno))
    except:
        print("error")
    db.close()
    '''
    sys.exit(app.exec_())