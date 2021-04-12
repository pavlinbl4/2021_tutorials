import asyncio
from aiogram import Bot


async def main():
    bot = Bot(token='1579508574:AAFOh6KvJZKoTQ11mdy1C6YiaBkOOPPju-4')

    try:
        me = await bot.get_me()
        print(f"🤖 Hello, I'm {me.first_name}.\nHave a nice Day!")
    finally:
        await bot.close()

asyncio.run(main())