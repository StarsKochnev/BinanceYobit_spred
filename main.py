import json

import requests
import asyncio
from  aiogram import Bot, Dispatcher, executor,types
import time
bot = Bot(token='5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI')
dp = Dispatcher(bot)

while True:
    key = "https://api.binance.com/api/v3/ticker/price?symbol=LTCRUB"
    data = requests.get(key)
    data = data.json()
    z = data['price']
    last_trade_binance = round(float(z))
    print(f"{data['symbol']} Binance цена: {data['price']}")

    key2 = "https://yobit.net/api/3/ticker/ltc_rur"
    data = requests.get(key2)
    data = data.json()
    b = data['ltc_rur']
    last_trade = int(round(b['last']))
    print(f"LTCRUB Yobit цена: {last_trade}")

    # считаем разницу

    percent = 100 / (last_trade - last_trade_binance) / last_trade_binance
    fg = str(percent)
    f = fg.replace('e-05', '')
    percent_fin = round(float(f), 3)
    print('Разница между курсами валют в %', percent_fin)
    time.sleep(1)
    percent_str = str(percent_fin) +' Разница достигла уровня покупки!!!! > 7%'

    # теперь отправляем наш % разница в телегу если разница курсов дошла до требуемого значения

    def send_msg(text):
       token = "5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI"
       chat_id = "688820140"
       url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
       results = requests.get(url_req)
       print(results.json())
    if percent_fin > 7:
        send_msg(percent_str)

    else:
        print('Разница в курсах меньше 10%')
    time.sleep(60)
