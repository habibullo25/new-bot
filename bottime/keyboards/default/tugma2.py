from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, reply_keyboard

tugma2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="gramm >>"),
            KeyboardButton(text="kilogramm >>"),
            KeyboardButton(text="sentner >>")
        ],
        [
            KeyboardButton(text="tonna >>"),
            KeyboardButton(text="funt >>"),
            KeyboardButton(text="karat >>")
        ],
         [
            KeyboardButton(text="Asosiy menuga"),
        ]
    ],
    resize_keyboard=True
)
