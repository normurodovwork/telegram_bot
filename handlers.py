from aiogram import types, F

from aiogram import Router
from aiogram.filters import CommandStart, Command
from Keyboards.keyboards import langs

handlers_router = Router()


@handlers_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(text="Hello 👋", reply_markup=langs)


@handlers_router.message(Command('help'))
async def help(message: types.Message):
    await message.answer('How can i help you')


@handlers_router.message(F.text.contains('🇷🇺'))
async def hello(message: types.Message):
    await message.answer('Привет как дела ?')
