# PyQT

# TkInter
# wxPython : https://wxpython.org/

# PyQT : https://riverbankcomputing.com/software/pyqt/intro
# 라이센스 정책 유의


# Hello PyQT

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)    # QApplicaion class의 객체 생성
print(sys.argv)                 # sys.argv의 경로를 보여준다

label = QLabel("Hello PyQt")
label.show()                    # .show() 메서드로 화면에 보여준다

app.exec_()                     # 이벤트 loop를 작동시킨다


# QPushButton

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

button = QPushButton("Hello PyQt")
button.show()

app.exec_()


# PyQT 위젯

# QGroupBox, QLabel
# QTextEdit, QDateEdit
# QTimeEdit, QLineEdit
# Window : QMainWindow 또는 QDialog (최상위 위젯)


# Window Class 정의 / Widgets 추가

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * # 아이콘 넣기 위해 불러오는 것

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()                  # super()
        self.setGeometry(100,100,400,400)   # Window 위치 지정
        self.setWindowTitle("가상화폐 자동매매 프로그램") # Window 타이틀바 변경

        buy_button = QPushButton("매수", self)                      # 버튼 1
        buy_button.move(20, 20)
        buy_button.clicked.connect(self.buy_button_clicked)         # 클릭 이벤트

        sell_button = QPushButton("매도", self)                     # 버튼 2
        sell_button.move(200, 20)
        sell_button.clicked.connect(self.sell_button_clicked)       # 클릭 이벤트

        self.setWindowIcon(QIcon("icon.png"))                       # 아이콘

    def buy_button_clicked(self):
        print("매수 버튼이 클릭됐습니다.")
        
    def sell_button_clicked(self):
        print("매도 버튼이 클릭됐습니다.")
    # 버튼 클릭시 호출 함수 정의 ("callback")
    
app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()


# 아이콘 넣기
# 아이콘 찾는 곳 : http://www.myiconfinder.com/

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock")
        self.setGeometry(300, 300, 300, 400)

        btn = QPushButton("클릭", self)
        btn.move(20, 20)
        btn.clicked.connect(self.btn_clicked)

        self.setWindowIcon(QIcon("icon.png"))

    def btn_clicked(self):
        print("버튼 클릭")

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()

# PyQT 참고 자료 : http://zetcode.com/gui/pyqt5/


# Telegram Bot 만들기

# "BotFather"에게 말을 걸고 token을 받는다
# import telepot
# 별도 PPT 참조

# 애드센스 달고 추천종목 제공하는 수익모델 가능

# 카카오봇 : web server 필요, 먼저 메세지 보낼 수 없다.


# Qt Designer

# Designer에서 만든 양식을 xml(.ui) 양식으로 저장
# 이벤트 처리 코드는 직접 작성 (Designer에서 객체명 확인)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("MyWindow.ui")[0] # .ui 파일 불러와서 클래스 생성

class MyWindow(QMainWindow, form_class): # 위의 form_class를 상속
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        # 직접 작성 : Qt Designer에서 확인한 버튼 객체명이 'pushButton'

    def btn_clicked(self): # 동작 함수도 만들어준다
        print("버튼 클릭")

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()



# ui 두번째 (Label / Line Edit / Push Button)

# pykorbit 설치 필요
# pip install pykorbit   (처음 설치 시)
# pip install pykorbit --upgrade (업그레이드)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit # korbit API에서 시세 불러오기 위함

form_class = uic.loadUiType("MyWindow2.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked) # 직접 작성

    def btn_clicked(self): # 직접 작성
        btc_price = pykorbit.get_current_price("btc_krw") # 시세를 불러와서
        eth_price = pykorbit.get_current_price("eth_krw")
        self.lineEdit.setText(str(btc_price)) # lineEdit 위에 출력
        self.lineEdit_2.setText(str(eth_price))

app = QApplication.instance()
if app is None : # Spyder에서 PyQT 실행시 오류 Kernel Die 해결
    app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()

# It failed JSONDecodeError : 그래도 뭔가 들어오긴 한다


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
        self.statusBar().showMessage(str_time) # 위치 : statusBar

app = QApplication.instance()
if app is None : # Spyder에서 PyQT 실행시 오류 Kernel Die 해결
    app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()



# 연습문제 1, 2

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

        self.timeout() # 시세 불러오는 시계
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.timer2 = QTimer(self) # statusBar 시계
        self.timer2.start(1000)
        self.timer2.timeout.connect(self.timeout_1sec)

    def timeout(self): # 시세 불러오기
        btc_price = pykorbit.get_current_price("btc_krw")
        eth_price = pykorbit.get_current_price("eth_krw")

        # pykorbit을 통해 얻어온 금액을 QLineEdit 객체에 출력하기
        self.lineEdit.setText(str(btc_price))
        self.lineEdit_2.setText(str(eth_price))

    def timeout_1sec(self): # statusBar 시계
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage("현재시간: " + str_time)

app = QApplication.instance()
if app is None : # Spyder에서 PyQT 실행시 오류 Kernel Die 문제 해결
    app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()


## Thread 문제를 잘 해결해야 원하는 성능 발휘한다

class Worker(QThread):
    finished = pyqtSignal(dict)
 
    def run(self):
        while True:
            data = {}
            self.finished.emit(data)
            self.msleep(500)
