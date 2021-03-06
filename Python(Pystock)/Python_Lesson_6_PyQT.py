# PyQT

# TkInter
# wxPython : https://wxpython.org/

# PyQT : https://riverbankcomputing.com/software/pyqt/intro
# ���̼��� ��å ����


# Hello PyQT

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)    # QApplicaion class�� ��ü ����
print(sys.argv)                 # sys.argv�� ��θ� �����ش�

label = QLabel("Hello PyQt")
label.show()                    # .show() �޼���� ȭ�鿡 �����ش�

app.exec_()                     # �̺�Ʈ loop�� �۵���Ų��


# QPushButton

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

button = QPushButton("Hello PyQt")
button.show()

app.exec_()


# PyQT ����

# QGroupBox, QLabel
# QTextEdit, QDateEdit
# QTimeEdit, QLineEdit
# Window : QMainWindow �Ǵ� QDialog (�ֻ��� ����)


# Window Class ���� / Widgets �߰�

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * # ������ �ֱ� ���� �ҷ����� ��

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()                  # super()
        self.setGeometry(100,100,400,400)   # Window ��ġ ����
        self.setWindowTitle("����ȭ�� �ڵ��Ÿ� ���α׷�") # Window Ÿ��Ʋ�� ����

        buy_button = QPushButton("�ż�", self)                      # ��ư 1
        buy_button.move(20, 20)
        buy_button.clicked.connect(self.buy_button_clicked)         # Ŭ�� �̺�Ʈ

        sell_button = QPushButton("�ŵ�", self)                     # ��ư 2
        sell_button.move(200, 20)
        sell_button.clicked.connect(self.sell_button_clicked)       # Ŭ�� �̺�Ʈ

        self.setWindowIcon(QIcon("icon.png"))                       # ������

    def buy_button_clicked(self):
        print("�ż� ��ư�� Ŭ���ƽ��ϴ�.")
        
    def sell_button_clicked(self):
        print("�ŵ� ��ư�� Ŭ���ƽ��ϴ�.")
    # ��ư Ŭ���� ȣ�� �Լ� ���� ("callback")
    
app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()


# ������ �ֱ�
# ������ ã�� �� : http://www.myiconfinder.com/

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock")
        self.setGeometry(300, 300, 300, 400)

        btn = QPushButton("Ŭ��", self)
        btn.move(20, 20)
        btn.clicked.connect(self.btn_clicked)

        self.setWindowIcon(QIcon("icon.png"))

    def btn_clicked(self):
        print("��ư Ŭ��")

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()

# PyQT ���� �ڷ� : http://zetcode.com/gui/pyqt5/


# Telegram Bot �����

# "BotFather"���� ���� �ɰ� token�� �޴´�
# import telepot
# ���� PPT ����

# �ֵ弾�� �ް� ��õ���� �����ϴ� ���͸� ����

# īī���� : web server �ʿ�, ���� �޼��� ���� �� ����.


# Qt Designer

# Designer���� ���� ����� xml(.ui) ������� ����
# �̺�Ʈ ó�� �ڵ�� ���� �ۼ� (Designer���� ��ü�� Ȯ��)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("MyWindow.ui")[0] # .ui ���� �ҷ��ͼ� Ŭ���� ����

class MyWindow(QMainWindow, form_class): # ���� form_class�� ���
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        # ���� �ۼ� : Qt Designer���� Ȯ���� ��ư ��ü���� 'pushButton'

    def btn_clicked(self): # ���� �Լ��� ������ش�
        print("��ư Ŭ��")

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()



# ui �ι�° (Label / Line Edit / Push Button)

# pykorbit ��ġ �ʿ�
# pip install pykorbit   (ó�� ��ġ ��)
# pip install pykorbit --upgrade (���׷��̵�)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit # korbit API���� �ü� �ҷ����� ����

form_class = uic.loadUiType("MyWindow2.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked) # ���� �ۼ�

    def btn_clicked(self): # ���� �ۼ�
        btc_price = pykorbit.get_current_price("btc_krw") # �ü��� �ҷ��ͼ�
        eth_price = pykorbit.get_current_price("eth_krw")
        self.lineEdit.setText(str(btc_price)) # lineEdit ���� ���
        self.lineEdit_2.setText(str(eth_price))

app = QApplication.instance()
if app is None : # Spyder���� PyQT ����� ���� Kernel Die �ذ�
    app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()

# It failed JSONDecodeError : �׷��� ���� ������ �Ѵ�


# Timer

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import * # timer

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time) # ��ġ : statusBar

app = QApplication.instance()
if app is None : # Spyder���� PyQT ����� ���� Kernel Die �ذ�
    app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()



# �������� 1, 2

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("mywindow2.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icon.png"))
        self.setupUi(self)

        self.timeout() # �ü� �ҷ����� �ð�
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.timer2 = QTimer(self) # statusBar �ð�
        self.timer2.start(1000)
        self.timer2.timeout.connect(self.timeout_1sec)

    def timeout(self): # �ü� �ҷ�����
        btc_price = pykorbit.get_current_price("btc_krw")
        eth_price = pykorbit.get_current_price("eth_krw")

        # pykorbit�� ���� ���� �ݾ��� QLineEdit ��ü�� ����ϱ�
        self.lineEdit.setText(str(btc_price))
        self.lineEdit_2.setText(str(eth_price))

    def timeout_1sec(self): # statusBar �ð�
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage("����ð�: " + str_time)

app = QApplication.instance()
if app is None : # Spyder���� PyQT ����� ���� Kernel Die ���� �ذ�
    app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()


## Thread ������ �� �ذ��ؾ� ���ϴ� ���� �����Ѵ�

class Worker(QThread):
    finished = pyqtSignal(dict)
 
    def run(self):
        while True:
            data = {}
            self.finished.emit(data)
            self.msleep(500)
