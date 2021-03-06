# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:15:26 2018

@author: Eunyoung
"""


# IF문


# IF / ELIF / ELSE

currency = 'xrp_krw'

if currency == "btc_krw":
    print("비트코인")
elif currency == "bch_krw":
    print("비트코인 캐시")
elif currency == "btg_krw":
    print("비트코인 골드")
elif currency == "eth_krw":
    print("이더리움")
elif currency == "xrp_krw":
    print("리플")
else :
    print("해당화폐)

  
# INPUT

age = input("나이를 입력하세요 : ")
print(age)


# 연습문제 1

num = input("입력: ")
num = int(num)
if num > 10 :
    print("10보다 크다")
else :
    print("10보다 크지 않다")


# FOR문

bitcoin = [720, 710, 580, 600, 620]
for i in bitcoin :
    print(i)

bitcoin = [720, 710, 580, 600, 620]
for i in bitcoin :
    print(bitcoin[i])
 
print(i) # i는 선언도 안 하고? bitcoin[i]로는 안 되고?

# r example
for i in c(1,3,5) { # 여기서도 첫번째, 두번째, ... 순차적으로 불러온다.
    print(bitcoin[i])
    }


# for와 딕셔너리

coins = {"bitcoin": 8600000, "ripple": 750}

for coin in coins:
    print(coin)

for k, v in coins.items():
    print(k, v)


# range

range(10) # list
type(range(10))

for i in range(5) : # list를 넣을 순 없다. range는 한 순간에 값을 하나만 준다
    print(i)

for i in list(range(5)) : # 이렇게 하면 안 된다는 말
    print(i)


# for와 range

tickers = ['BTC', 'XRP', 'LTC']

# 방법 1 - 리스트값 바로 불러오기
for ticker in tickers:
    print(ticker)

# 방법 2 - 인덱싱
for i in range(len(tickers)):
    ticker = tickers[i]
    print(ticker)


# 연습문제
    
interest_stocks = ["Naver", "Samsung", "SK Hynix"]
for i in interest_stocks :
    print(i)

prices = [300, 400, 2000, 2400]
for i in prices :
    if i > 1000 :
        print(i)

prices = ["300", "400", "2000", "2400"]
for i in prices :
    if len(i) >= 4 :
        print(i)

a = int(0)
for i in range(20) : # range(19) 하면 안 되네?
    a += 1
    print(a)

    
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = int()
for i in A :
    sum += i
print(sum/len(A))


# WHILE문
# loop의 횟수가 정해져있지 않을 때. 무한루프

while True :
    print("수업중")
# Ctrl + C 로 잘 안 멈춘다!

for i in range(1, 6) :
    print(i)

num = 1
while num <= 5 :
    print(num)
    num += 1

# 연습문제
price = 10000
day = 1
while day <= 5 :
    price *= 1.3
    day += 1
print(price)

# lotto 자동번호 추출 
# 1~45까지의 숫자 6개를 생성하기 
# 숫자는 중복으로 생성될 수 없음

import random

for i in range(6) :
    num = random.randint(1, 45)
    print(num)
# 중복 문제 해결 필요

lotto = []
for i in range(6) :
    num = random.randint(1, 45)
    if num not in lotto :
        lotto.append(num)
    else :
        print(num)
print(lotto)
# 횟수 제한 문제가 남았다

# while문으로 만들어보자!


# 함수

# 함수 정의
def 별찍기() :
    print("******")

별찍기
print(별찍기) # '별찍기'는 코드의 메모리 위치를 저장
별찍기()

def 별찍기(num) :
    print("*" * num)

별찍기(3)
별찍기() # TypeError: 별찍기() missing 1 required positional argument: 'num'

# 코드가 여러 줄 되면 함수로 정의하자. 코드의 의미 알아보기 편하도록


def generate_url(code):
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    return url

url =generate_url("073240")     # 함수 호출 
print(url)

codes = ["000660", "039490"]

for code in codes:
    url = generate_url(code)    # 종목 코드를 입력 받아 url를 생성
    data = request_by_url(url)  # url로부터 데이터를 요청 : 여기선 미정의
    print(data)


def hap(a, b):
    t = a + b
    return t

hap(3, 4)


# 연습문제 1

def mul(a, b) :
    return a * b

mul(100, 4)

# ??????
def my_sum(list(a)) :
    return sum(a))

my_sum([1,3])


# Module
# 파이썬 소스 코드 파일이 바로 "모듈"


import datetime
datetime.datetime.now()

now = datetime.datetime.now()
now1 = str(now)
print(now1)
now1[:1]


import time
time.sleep(1)


import time
import datetime

while True :
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)


# module importing 방법
import os # os.listdir - 이 방법을 가장 선호. 모듈별로 이름 중복 가능성 때문
from os import listdir # listdir
from os import * # listdir
import os as myos # myoslistdir - 이것도 가끔 쓴다
# 남들이 주로 쓰는 import 방법을 쓰는 게 좋다
# ex) import matplotlibpyplot as plt - 모두가 plt라고 쓰니까 나도 plt로


# module을 만들어보자

import mymodule

mymodule.get_ma5()


# 좀 더 좋은 모듈을 만들어보자

import requests

payload = {"currency_pair": "btc_krw"}
url = "https://api.korbit.co.kr/v1/ticker"
r = requests.get(url, params=payload)
contents = r.json()
price = contents['last']
print(price)
# https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw


# 함수로 선언해보자
def get_last_price(ticker) :
    payload = {"currency_pair": ticker}
    url = "https://api.korbit.co.kr/v1/ticker"
    r = requests.get(url, params=payload)
    contents = r.json()
    price = contents['last']
    return price

get_last_price("btc_krw")
get_last_price("xrp_krw")
get_last_price("ltc_krw")


# ma(5)를 구하는 모듈을 만들어보자
import stock
ma5([3,4,5,6,7,8,9])


import pybithumb # 모듈이 설치되어 있어야 함
pybithumb.get_tickers()
