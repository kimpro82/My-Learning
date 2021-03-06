# 6주차 - 2018-12-16

# 파일 다루기

# READ

f = open('C:/Users/Eunyoung/PycharmProjects/MyProject/buy_list.txt', 'rt', encoding='utf-8')

f = open("buy_list.txt", encoding='utf-8')
lines = f.readlines()
f.close()

for line in lines:
    s = line.strip()        # 공백, \n
    print(s)

with open("buy_list.txt") as f:       # 이런 식으로 많이 사용한다
    lines = f.readlines()
# 왜 안 되지

# 대용량 파일은 readlines()로 무리


# WRITE

f = open("sell_list.txt", "wt", encoding='utf-8')

f.write("미래에셋대우\n") # \n 행갈이까지 입력
f.write("LG전자\n")

f.close()


# Back Testing


# 일봉 데이터 가져오기

import pybithumb

df = pybithumb.get_ohlcv("BTC")
print(df.tail())

df.to_excel("data01.xlsx")


# 이동평균

import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['ma5'] = df['close'].rolling(window=5).mean()    # 5일 이동평균

df.to_excel("data02.xlsx")


# 상승장/하락장 판단

import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['ma5'] = df['close'].rolling(window=5).mean()
df['ma5_shift1'] = df['ma5'].shift(1)           # 'ma5'를 밑으로 한 줄 내린다
df['bull'] = df['open'] > df['ma5_shift1']
df.to_excel("data03.xlsx")


# 변동성 계산

import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['ma5'] = df['close'].rolling(window=5).mean()
df['ma5_shift1'] = df['ma5'].shift(1)
df['bull'] = df['open'] > df['ma5_shift1']

# 변동성
df['volatility'] = (df['high'] - df['low']) * 0.5
df.to_excel("data04.xlsx")


# 목표가 계산

import pybithumb

df = pybithumb.get_ohlcv("BTC")
df['ma5'] = df['close'].rolling(window=5).mean()
df['ma5_shift1'] = df['ma5'].shift(1)
df['bull'] = df['open'] > df['ma5_shift1']

# 변동성
df['volatility'] = (df['high'] - df['low']) * 0.5
# 목표가
df['target'] = df['open'] + df['volatility'].shift(1)

df.to_excel("data05.xlsx")


# 수익률 계산

import pybithumb
import numpy as np  # numpy 불러오기

# 변동성
df['volatility'] = (df['high'] - df['low']) * 0.5
# 목표가
df['target'] = df['open'] + df['volatility'].shift(1)
# 수익률
df['er'] = np.where(df['bull'] & (df['high’] >= df['target']),
                                   df['close'] / df['target'],
                                   1)
# numpy에선 IF문 대신 np.where(contition, x, y)를 사용한다

df.to_excel("data06.xlsx")


# 누적수익률 계산

# cumprod()
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.cumprod.html

import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")
df['ma5'] = df['close'].rolling(window=5).mean()
df['ma5_shift1'] = df['ma5'].shift(1)
df['bull'] = df['open'] > df['ma5_shift1']

# 변동성
df['volatility'] = (df['high'] - df['low']) * 0.5
# 목표가
df['target'] = df['open'] + df['volatility'].shift(1)
# 수익률
df['er'] = np.where(df['bull'] & (df['high'] > df['target']),
                                  df['close'] / df['target'],
                                  1)
df['cumprod'] = df['er'].cumprod()

print("누적수익률 (배): ", df['cumprod'].iloc[-1])
    # 장이 아직 안 끝났으니 어제까지의 수익률을 구하려면 [-2] 대입
df.to_excel("data07.xlsx")


# 2018년 리플 벡테스팅

import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("XRP")
df = df['2018']                                                 # 리플 일봉 중 2018년도

df['ma5'] = df['close'].rolling(window=5).mean()                # 5일 이동평균 컬럼
df['ma5_shift1'] = df['ma5'].shift(1)                           # 5일 이동평균 컬럼에서 하나씩 내림
df['bull'] = df['open'] > df['ma5_shift1']                      # 상승장/하락장 판단

df['volatility'] = (df['high'] - df['low'])*0.5                 # 변동성 * 0.5
df['target'] = df['open'] + df['volatility'].shift(1)           # 목표가 = 시가 + 전일 변동성 * 0.5
df['er'] = np.where(df['bull'] & (df['high'] >= df['target']),  # 매수 조건
                    df['close'] / df['target'],                 # 매수시 수익률 (매도가/매수가)
                    1)                                          # 홀드시 수익률
df['cumprod'] = df['er'].cumprod()

# 엑셀 파일로 저장
print("누적수익률(배): ", df['cumprod'][-2])
df.to_excel("data08.xlsx")



# 가장 수익률 좋았던 코인은?

import pybithumb
import numpy as np


def run_volatility_breakout(ticker):
    df = pybithumb.get_ohlcv(ticker)
    df = df['2018']                                                 # 일봉 중 2018년도

    df['ma5'] = df['close'].rolling(window=5).mean()                # 5일 이동평균 컬럼
    df['ma5_shift1'] = df['ma5'].shift(1)                           # 5일 이동평균 컬럼에서 하나씩 내림
    df['bull'] = df['open'] > df['ma5_shift1']                      # 상승장/하락장 판단

    df['volatility'] = (df['high'] - df['low'])*0.5                 # 변동성 * 0.5
    df['target'] = df['open'] + df['volatility'].shift(1)           # 목표가 = 시가 + 전일 변동성 * 0.5
    df['er'] = np.where(df['bull'] & (df['high'] >= df['target']),  # 매수 조건
                        df['close'] / df['target'],                 # 매수시 수익률 (매도가/매수가)
                        1)                                          # 홀드시 수익률
    df['cumprod'] = df['er'].cumprod()
    return df['cumprod'][-2]


tickers = pybithumb.get_tickers()
result = []

for ticker in tickers:
    earning_rate = run_volatility_breakout(ticker)
    result.append((ticker, earning_rate))
# 왜 오류가 나올까

# 정렬
ranked_data = sorted(result, key=lambda x:x[1], reverse=True)
print(ranked_data)



