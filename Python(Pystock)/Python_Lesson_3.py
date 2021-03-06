# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:52:01 2018

@author: Eunyoung
"""

# 2018-11-25 (3주차)


# 1. 연습문제


# Q1. 딕셔너리

Min_Quantity = {"BTC" : 0.001,
                "ETH" : 0.01,
                "DASH" : 0.01,
                "LTC" : 0.01,
                "ETC" : 0.1,
                "XRP" : 10,
                "BCH" : 0.001
                }


# Q2. 딕셔너리 인덱싱

print("BTC", Min_Quantity["BTC"])
print("ETH", Min_Quantity["ETH"])

for m, n in Min_Quantity.items() :
    print(m, n)


# Q3. 공백제거

mylist = ['  abc   ', '   def    ', ' kkk   ']

for i in mylist :
    print(i.strip())


# Q4. datetime 모듈

import datetime

def get_current_time() :
    now = datetime.datetime.now()
    print(str(now)[1:19])

get_current_time()


# Q5. datetime - 익일 00:00:00

import datetime

now = datetime.datetime.now()
target_time = datetime.datetime(year=now.year, 
                                month=now.month,
                                day=now.day+1, 
                                hour=0,
                                minute=0,
                                second=0)
print(target_time)


# Q6. 딕셔너리 인덱싱

all = {'BTC': {'opening_price': '6436000',
               'closing_price': '6404000',
               'min_price': '6372000',
               'max_price': '6455000',
               'average_price': '6416495.9956',
               'units_traded': '816.08087921',
               'volume_1day': '816.08087921',
               'volume_7day': '16413.04357476',
               'buy_price': '6406000',
               'sell_price': '6413000',
               '24H_fluctate': '-32000',
               '24H_fluctate_rate': '-0.49'}}

print(all['BTC']['opening_price'])
print(all['BTC']['closing_price'])


# Q7. 딕셔너리 Key값 대/소문자 변경

tickers = ['btc', 'xrp', 'ltc']

def change_tickers(tickers):
    result = []
    for i in tickers :
        result.append(i.upper())
    return result

new_tickers = change_tickers(tickers)
print(new_tickers)


# Q8 딕셔너리

production_year = [2014, 2015, 2014, 2013, 2016, 2018, 2017, 2017]

count = {}
for i in production_year :
    if i in count.keys() :
        count[i] += 1
    else :
        count[i] = 1

print(count)


# Q9

def final_url(code) :
    url = 'https://finance.naver.com/item/main.nhn?code='
    return url + code
    
final_url('000020')

# '000020'에서 ''를 빼면 SyntaxError : invalid token
# 함수에 str()을 쓰고 000020(int)을 입력할 순 없을까
# (앞에 0이 붙은) 000020 같은 형태의 숫자는 없다!

def concatenate(a, b) :
    return a + str(b)

concatenate('기안', 84)
# 출력 : 기안84 (정상)


# 나머지 연습 문제는 각자 해보자!



# 2. Class 1


# 클래스 정의 및 객체 생성

class MyClass :
    pass

obj1 = MyClass()
obj2 = MyClass()
print(id(obj1))
print(id(obj2))

# 관례적으로 사용자 정의 클래스는 대문자 사용


# 메서드(method)

class MyClass :
    def foo(self) :
        print("메서드 호출")

# 메서드의 첫번째 인자는 무조건 self

a = MyClass()
a.foo()


# 인스턴스 변수

class MyClass:
    pass

a = MyClass()
b = MyClass()

a.val = 3
b.val = 4

print(a.val)
print(b.val)


# 생성자


class Customer :
    def __init__(self):
        print("계좌 생성")

kim = Customer()
lee = Customer()


class MyClass:
    def __init__(self):
        self.var = 0

obj1 = MyClass()
obj2 = MyClass()

print(obj1.var)
print(obj2.var)


class Customer :
    def __init__(self, balance) :
        self.balance = balance

kim = Customer(100)
lee = Customer(200)

print(kim.balance)
print(lee.balance)



# 점(.)의 의미
# 속성 참조 순서 : 인스턴스 - 클래스 - 부모 클래스 


# 연습문제

class Customer :
    def __init__(self, name, balance) :
        self.name = name
        self.balance = balance

    def deposit(self, money) :
        self.balance = self.balance + money

    def withdraw(self, money) :
        self.balance = self.balance - money
    

kim = Customer('김아무개',1000)
print(kim.name, kim.balance)

kim.deposit(1000)
print(kim.name, kim.balance)



# 3. Class 3


# What is the self ?

# self는 메서드의 첫번째 인자로 사용됨 
# self는 메서드를 호출한 객체를 바인딩하는 변수

class MyClass :
    def my_method(self) :
        print("메서드호출 : ", self)

obj1 = MyClass()
obj1.my_method()       # self는 obj1
id(obj1)
0x21803bb9e8


class 붕어빵틀 :
    def 팥소넣기(self, 팥소) :
        self.팥소 = 팥소
        
붕어빵1 = 붕어빵틀()
붕어빵2 = 붕어빵틀()

# 메서드 호출
붕어빵틀.팥소넣기(붕어빵1, "초코맛팥소")
붕어빵틀.팥소넣기(붕어빵2, "딸기맛팥소")

# 붕어빵 맛 확인하기
print(붕어빵1.팥소)
print(붕어빵2.팥소)


# 클래스.메서드(객체, 데이터) 와 객체.메서드(데이터)는 같은 표현임.


# 객체 참조 순서

class Customer:
    name = "기본값" # 모든 객체가 참조해야 하는 값은 여기에 저장

# 그러나 이렇게 쓸 일은 잘 없다. self를 잘 이해하지 못 한 경우

a = Customer()
a.name = "kim"

b = Customer()

print(a.name) # "kim"
print(b.name) # "기본값"


# self가 없다면

class Customer:
    def __init__(self, name):
        name2 = name

c = Customer("kim")
print(c.name2)  # AttributeError : has no 'name2'


# 연습문제 1

class Student :
    def __init__(self, name, grade, major, toeic):
        self.name = name
        self.grade = grade
        self.major = major
        self.toeic = toeic

    def set_name(self, name) :
        self.name = name

    def set_grade(self, grade) :
        self.grade = grade

    def set_major(self, major) :
        self.major = major

    def set_toeic(self, toeic) :
        self.toeic = toeic

kim = Student("김아무개","A+","철학과","990")
print(kim.name, kim.grade, kim.major, kim.toeic)

kim.set_name("김누구")
print(kim.name, kim.grade, kim.major, kim.toeic)


# 상속(inheritance)


# Parent에게 sing method가 있다

class Parent:
    def sing(self):
        print("sing a song")

class LuckyChild(Parent):
    pass

luckyboy = LuckyChild()
luckyboy.sing()


# Parent에게 sing method가 없다

class UnLuckyChild:
    pass

unluckyboy = UnLuckyChild()
unluckyboy.sing()


# 좋은 케이스 : 노래 실력은 물려받았고 춤은 노력으로 습득

class Parent:
    def sing(self):
        print("sing a song")

class LuckyChild(Parent):
    def dance(self):
        print("shuffle dance")

luckyboy = LuckyChild()
luckyboy.sing()
luckyboy.dance()


# 다음주에는 data scrapping & pandas(dataframe)