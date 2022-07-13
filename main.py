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

    percent = int(100) / (last_trade - last_trade_binance) / last_trade_binance * int(100000)
    percent2 = round(percent, 2)
    print('Разница между курсами валют в %', percent2)
    time.sleep(1)
    percent_str = str(percent2) + ' Разница достигла уровня покупки!!!! > 7%' + str()

    # теперь отправляем наш % разница в телегу если разница курсов дошла до требуемого значения

    def send_msg(text):

       token = "5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI"
       chat_id = "688820140"
       url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
       results = requests.get(url_req)
       print(results.json())
    if percent2 < 7 or percent2 > 10:
        send_msg(percent_str)

    else:
        print('Разница в курсах меньше 7 или больше 10')
    time.sleep(60)
