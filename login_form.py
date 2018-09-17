import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QPushButton
from login import Ui_form
from testbtn import Ui_Form
from logintest import Ui_Dialog2
#登陆页面

class login_form(QtWidgets.QWidget,Ui_form):
    def __init__(self):
        super(login_form, self).__init__()
        self.setupUi(self)

    def jump(self):
        self.close()
        self.m2 = jump_test()
        self.m2.exec_()

'''
class btn_test(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(btn_test, self).__init__()
        self.setupUi(self)

    def jump(self):
        self.close()
        self.m2 = jump_test()
        self.m2.exec_()
'''


#跳转页面
class jump_test(QtWidgets.QDialog,Ui_Dialog2):
    def __init__(self):
        super(jump_test, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_login_form = login_form()
    #my_login_form.pushButton.click()
    #显示登陆页面
    my_login_form.show()
    sys.exit(app.exec_())