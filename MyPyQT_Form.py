import sys
from PyQt5 import QtWidgets
from pyqt_form import Ui_Form

class MyPyQt_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQt_Form,self).__init__()
        self.setupUi(self)

    def pushButton_click(self):
        self.textEdit.setText("你点击按钮了")
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQt_Form()
    my_pyqt_form.show()
   # my_pyqt_form.pushButton.
    sys.exit(app.exec_())
