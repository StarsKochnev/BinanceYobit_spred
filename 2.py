from  aiogram import Bot, Dispatcher, executor,types
import time
bot = Bot(token='5555491875:AAH-aKzegGa2ZGnKrnbvllac-tRueXQPzMI')
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    while True:
        resp_msg = 'ghgfhgfh'
        await message.answer(resp_msg)
        time.sleep(1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)