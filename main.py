import time

import json
import requests

import os

#def parse(url):
    #api = requests.get(url)
    #tree = lxml.html.document_fromstring(api.text)
    #text_original = tree.xpath('//*[@id="label_bestsell"]/text()')
    #print(type(text_original))
    #print('Продажа Ltc- rub', text_original)

#parse('https://yobit.biz/ru/trade/LTC/RUR#24H')



# defining key/request url
while True:
    key = "https://api.binance.com/api/v3/ticker/price?symbol=LTCRUB"

    # requesting data from url
    data = requests.get(key)
    data = data.json()
    z = data['price']
    last_trade_binance = round(float(z))
    print(last_trade_binance)


    print(f"{data['symbol']} price is {data['price']}")
    key2 = "https://yobit.net/api/3/ticker/ltc_rur"
    data = requests.get(key2)
    data = data.json()
    #print(data)
    b = data['ltc_rur']

    last_trade = int(round(b['last']))

    print(f"Yobit {last_trade}")

    percent = 100 / (last_trade - last_trade_binance) / last_trade_binance
    fg = str(percent)
    f = fg.replace('e-05', '')
    y = round(float(f), 3)
    print(y)
    print('Разница между курсами валют в %', y)
    time.sleep(2)
