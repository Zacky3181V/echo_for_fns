import logging
from key import TOKEN
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot=Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    await message.reply("Привет!\nЯ эхо бот!")

@dp.message_handler(commands=['help'])
async def ask_for_help(message:types.Message):
    await message.reply("Пиши мне что угодно и я отвечу этим же сообщением")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
