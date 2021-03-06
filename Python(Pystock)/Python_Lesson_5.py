import pybithumb
import time
import datetime


# API Key 입력
key = "fc7f66c91bcf38d9e64f3eb2fb3fde6b"
secret = "a583820ef5b76b7c4afe909176c80666"

bithumb = pybithumb.Bithumb(key, secret)
print(bithumb)

# 잔고 조회
bithumb = pybithumb.Bithumb(key, secret)
balance = bithumb.get_balance("ETH")
print(balance)
krw_balance = balance[2]


# 매수 호가 조회
orderbook = pybithumb.get_orderbook("BTC")
bids = orderbook['bids']

for bid in bids:
    print(bid['quantity'], bid['price'])


# 매수함수 구현
def try_buy(now, cur_price, target_price):
    krw_balance = bithumb.get_balance("BTC")[2]

    # 최우선 매도호가의 가격 얻기
    orderbook = pybithumb.get_current_price("BTC")
    asks = orderbook['asks']
    price0 = asks[0]['price']
    unit = krw_balance / price0

    if cur_price >= target_price:
        bithumb.buy_market_order("BTC", unit)
