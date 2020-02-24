import sys
from PySide2.QtWidgets import QApplication, QMainWindow,QPushButton
from PySide2.QtCore import QFile
from mbti import *
import _pickle as pickle
import shelve


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.E.toggled.connect(lambda: self.btnstate())
        self.ui.I.toggled.connect(lambda: self.btnstate())
        self.ui.S.toggled.connect(lambda: self.btnstate())
        self.ui.N.toggled.connect(lambda: self.btnstate())
        self.ui.T.toggled.connect(lambda: self.btnstate())
        self.ui.F.toggled.connect(lambda: self.btnstate())
        self.ui.J.toggled.connect(lambda: self.btnstate())
        self.ui.P.toggled.connect(lambda: self.btnstate())

    def btnstate(self):
        if self.ui.E.isChecked():
            mbti[0] = 'e'
            self.ui.b1.clicked.connect(self.b1)
        elif self.ui.I.isChecked() :
            mbti[0]='i'
            self.ui.b1.clicked.connect(self.b1)
        if self.ui.N.isChecked():
            mbti[1] = 'n'
            self.ui.b2.clicked.connect(self.b2)
        elif self.ui.S.isChecked():
            mbti[1] = 's'
            self.ui.b2.clicked.connect(self.b2)
        if self.ui.T.isChecked():
            mbti[2] = 't'
            self.ui.b3.clicked.connect(self.b3)
        elif self.ui.F.isChecked():
            mbti[2] = 'f'
            self.ui.b3.clicked.connect(self.b3)
        if self.ui.J.isChecked():
            mbti[3] = 'j'
            self.ui.b4.clicked.connect(self.b4)
        elif self.ui.P.isChecked():
            mbti[3] = 'p'
            self.ui.b4.clicked.connect(self.b4)




    def b1(self):
        window.ui.stackedWidget.setCurrentIndex(1)

    def b2(self):
        window.ui.stackedWidget.setCurrentIndex(2)

    def b3(self):
        window.ui.stackedWidget.setCurrentIndex(3)
    def b4(self):
        self.ui.un.hide()
        self.ui.l1.hide()
        self.ui.l2.hide()
        un = self.ui.un.toPlainText()
        data = {'Name': un, 'MBTI': mbti}
        s = shelve.open('database')
        with open('myfile.txt', 'w') as f:
            print(data, file=f)
        s[un] = data
        self.ui.dis.setText("Hi "+ un +" your are an ")
        if mbti==['e','s','t','j']:
            window.ui.stackedWidget.setCurrentIndex(4)
        elif mbti==['e','n','t','j']:
            window.ui.stackedWidget.setCurrentIndex(5)
        elif mbti==['e','s','f','j']:
            window.ui.stackedWidget.setCurrentIndex(6)
        elif mbti==['e','s','t','p']:
            window.ui.stackedWidget.setCurrentIndex(7)
        elif mbti==['e','n','f','j']:
            window.ui.stackedWidget.setCurrentIndex(8)
        elif mbti==['e','n','t','p']:
            window.ui.stackedWidget.setCurrentIndex(9)
        elif mbti==['e','s','f','p']:
            window.ui.stackedWidget.setCurrentIndex(10)
        elif mbti==['e','n','f','p']:
            window.ui.stackedWidget.setCurrentIndex(11)
        elif mbti==['i','n','f','p']:
            window.ui.stackedWidget.setCurrentIndex(12)
        elif mbti==['i','s','f','p']:
            window.ui.stackedWidget.setCurrentIndex(13)
        elif mbti==['i','n','t','p']:
            window.ui.stackedWidget.setCurrentIndex(14)
        elif mbti==['i','n','f','j']:
            window.ui.stackedWidget.setCurrentIndex(15)
        elif mbti == ['i', 'n', 't', 'j']:
            window.ui.stackedWidget.setCurrentIndex(16)
        elif mbti == ['i', 's', 'f', 'j']:
            window.ui.stackedWidget.setCurrentIndex(17)
        elif mbti == ['i', 's', 't', 'p']:
            window.ui.stackedWidget.setCurrentIndex(18)
        elif mbti == ['i', 's', 't', 'j']:
            window.ui.stackedWidget.setCurrentIndex(19)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    mbti = ['0', '0', '0', '0']
    un = 'name'
    sys.exit(app.exec_())