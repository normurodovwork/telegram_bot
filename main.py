import os
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from handlers import handlers_router

load_dotenv()

dp = Dispatcher()
TOKEN = os.getenv('TOKEN')

dp.include_router(handlers_router)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())