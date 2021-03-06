# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


# Downloading HTML : requests
url = "http://finance.naver.com/item/main.nhn?code=000660"
print(requests.get(url)) # Response라는 이름의 객체가 나온다
html = requests.get(url).text
print(html) # the same with the original HTML code


# Parsing : BS (BS class의 object 생성)
soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#_dvr")
print(tags) # [<em id="_dvr">1.44</em>]
em_tag = tags[0]
print(em_tag.text, type(em_tag.text)) # 1.44 <class 'str'>


# Excersise : parsing PER
soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#_per")
print(tags) # [<em id="_per">4.76</em>]
em_tag = tags[0]
print(em_tag.text, type(em_tag.text)) # 4.76 <class 'str'>


# Chrome에서 구하고자 하는 데이터 '검사' → Copy Selector
# 단, BS에선 nth-child 지원하지 않으므로 다른 방법 찾아야


# 외국인 소진율을 가져와보자
tags = soup.select("#tab_con1 > div.gray > table > tbody > tr.strong > td > em")
#tags = soup.select("#tab_con1 > div:nth-of-type(2) > table > tbody > tr.strong > td > em")
print(tags[0].text)


# Default Argument

def hap2(a, b=3):
    return a + b

ret = hap2(3)
print(ret) # 6

ret2 = hap2(4, 5)
print(ret2) # 9


# Korbit API
# https://apidocs.korbit.co.kr/ko/
# https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw

# * timestamp : 1970-01-01부터 기록
# 대략 15억 정도면 초 단위
# 15조 정도면 ms 단위

# HTTP SET/POST 프로토콜


# KORBIT 최종 체결가

import requests

payload = {"currency_pair" :"btc_krw"}
url = "https://api.korbit.co.kr/v1/ticker"

r = requests.get(url, params=payload)
print(r.text, type(r.text))
# {"timestamp":1543728371816,"last":"4655500"} <class 'str'>

# JSON to Dictionary
contents = r.json()
print(contents, type(contents))
# {'timestamp': 1543728371816, 'last': '4655500'} <class 'dict'>

# 응용
print('비트코인 현재가 : ', contents['last'])
# 비트코인 현재가 :  4655500

# 시간 가져오기
import datetime
timestamp = contents['timestamp']
cur_time = datetime.datetime.fromtimestamp(timestamp/1000) # ms to sec
print(cur_time, type(cur_time))
# 2018-12-02 14:26:11.816000 <class 'datetime.datetime'>


# 연습문제 - 실패???
pairs = ("btc_krw", "bch_krw", "etc_krw")
payload = {"currency_pair" : pairs}
print(payload, type(payload))
# {'currency_pair': ('btc_krw', 'bch_krw', 'etc_krw')} <class 'dict'>
url = "https://api.korbit.co.kr/v1/ticker"

r = requests.get(url, params=payload)

for r in pairs : 
    print(r, ontents)



# Pandas
# R의 dataframe 자료구조를 Python에 이식
# 새롭지 않다!

from pandas import Series # 가장 많이 쓰는 importing 방법

data = [100, 200, 300]
data *3 # [100, 200, 300, 100, 200, 300, 100, 200, 300]
# ?????

s = Series(data)
print(s, type(s))
print(s * 3)
# 0    300
# 1    600
# 2    900
# dtype: int64


# index 부여

s = Series([8286500, 8146000, 7430000, 7410000, 7433000],
           index=['2018-04-13', '2018-04-12', '2018-04-11', '2018-04-10', '2018-04-09'])

print(s[0])
print(s['2018-04-13'])
print(s[[0,2,4]])
print(s['2018-04-13':'2018-04-11'])                     


# Dataframe 생성

from pandas import DataFrame

raw_data = {'open': [100, 90, 80, 70],
        'high': [110, 112, 90, 80],
        'low' : [90, 80, 70, 60],
        'close': [95, 85, 75, 63]}
df = DataFrame(raw_data)
print(df)

df = DataFrame(raw_data, columns=['open', 'high', 'low', 'close'])
print(df)
# 파이썬 3.7 이전 버전에선 딕셔너리에 순서 존재 X, 따로 지정해주면 좋다.


# 엑셀로 보내기
df.to_excel("dump.xlsx")
# saved at root directory


# 날짜는 날짜데이터로 넣자
# 아래 예시는 날짜를 datetime으로 받아오는 과정이 더 필요함
date_list = ['2018-04-14', '2018-04-13', '2018-04-12', '2018-04-11']
df = DataFrame(raw_data, columns=['open', 'high', 'low', 'close'], index=date_list)
print(df)
print(df['open'])
print(df[['open', 'close']])

df04 = df['2018-04'] # 이 상태로는 실행 X
df04.iloc[0]


# datetime.strptime()
import datetime

date = '2018-12-02'

date2 = datetime.datetime.strptime(date, '%Y-%m-%d')
print(date2, type(date2))
# 2018-12-02 00:00:00 <class 'datetime.datetime'>


# pybithumb 설치
# Anaconda Prompt에서
# python -m pip install Pybithumb -- upgrade pip

import pybithumb

df = pybithumb.get_ohlcv("BTC")
print(df)
print(df['2018-12-02'])


