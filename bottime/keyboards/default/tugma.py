from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, reply_keyboard

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Og'irlik bilan ishlash"),
        ],
        [
            KeyboardButton(text="Hajm bilan ishlash")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
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
    resize_keyboard=True,
    one_time_keyboard=True
)

tugma3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="millimetr kub >>"),
            KeyboardButton(text="santimetr kub >>"),
            KeyboardButton(text="detsimetr kub >>"),
            KeyboardButton(text="metr kub >>")
            
        ],
        [
            KeyboardButton(text="litr >>"),
            KeyboardButton(text="gektolitr >>"),
            KeyboardButton(text="yard kub >>"),
            KeyboardButton(text="fut kub >>")
        ],
         [
            KeyboardButton(text="Asosiy menuga"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

tugma4 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=">> gramm"),
            KeyboardButton(text=">> kilogramm"),
            KeyboardButton(text=">> sentner")
        ],
        [
            KeyboardButton(text=">> tonna"),
            KeyboardButton(text=">> funt"),
            KeyboardButton(text=">> karat")
        ],
         [
            KeyboardButton(text="Asosiy menuga"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

tugma5 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=">> millimetr kub"),
            KeyboardButton(text=">> santimetr kub"),
            KeyboardButton(text=">> detsimetr kub"),
            KeyboardButton(text=">> metr kub")
            
        ],
        [
            KeyboardButton(text=">> litr"),
            KeyboardButton(text=">> gektolitr"),
            KeyboardButton(text=">> yard kub"),
            KeyboardButton(text=">> fut kub")
        ],
         [
            KeyboardButton(text="Asosiy image.pngmenuga"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)