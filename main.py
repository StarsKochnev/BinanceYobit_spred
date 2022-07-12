import json
import requests
import asyncio
from  aiogram import Bot, Dispatcher, executor,types
import time

bot = Bot(token='5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI')
dp = Dispatcher(bot)
#from  aiogram import Bot, Dispatcher, executor,types
#bot = Bot(token='5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI')
#dp = Dispatcher(bot)
#def parse(url):
    #api = requests.get(url)
    #tree = lxml.html.document_fromstring(api.text)
    #text_original = tree.xpath('//*[@id="label_bestsell"]/text()')
    #print(type(text_original))
    #print('Продажа Ltc- rub', text_original)

#parse('https://yobit.biz/ru/trade/LTC/RUR#24H')
# defining key/request url

key = "https://api.binance.com/api/v3/ticker/price?symbol=LTCRUB"
# requesting data from url
data = requests.get(key)
data = data.json()
z = data['price']
last_trade_binance = round(float(z))
print(f"{data['symbol']} Binance цена: {data['price']}")

key2 = "https://yobit.net/api/3/ticker/ltc_rur"
data = requests.get(key2)
data = data.json()
#print(data)
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

#@dp.message_handler(commands="test1")
#async def cmd_test1(message: types.Message):
    #await message.reply("Test 1")
@dp.message_handler()
async def echo(message: types.Message):
    while True:
        if percent_fin > 1:
            resp_msg = percent_fin
            await message.answer(resp_msg)
            time.sleep(5)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






    #executor.start_polling(dp, skip_updates=True)

