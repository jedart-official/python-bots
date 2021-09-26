import logging
from config import*
from aiogram import Dispatcher, bot, dispatcher, executor, types
bot = Bot(token = "1867595092:AAE2G7LpMuno9EoOCoOxqM6qa0zjp1PnV-o")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands = ["start"])
async def start(message: types.Message):
    await message.answer("Отвечаю")

async def start2(message: types.Message):
    await message.answer("Отвечаю два")

dp.register_message_handler(start2, regexp = "Привет")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)