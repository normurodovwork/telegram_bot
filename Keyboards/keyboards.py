from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

langs = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🇷🇺 Русский'),
         KeyboardButton(text='🇺🇿 O\'zbekcha'),
         KeyboardButton(text='🇬🇧 English')],
    ],
    resize_keyboard=True
)