# from config import tg_bot_token
from config.py import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет!это тестовый бот aiogram")




if __name__ == '__main__':
    executor.start_polling(dp)