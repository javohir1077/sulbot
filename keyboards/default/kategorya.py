from cgitb import text
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍️ Каталог")],
        [KeyboardButton(text="Savatcha 🛒"),KeyboardButton(text="💰 Баланс")],
        [KeyboardButton(text="Buyurtma berish 🚚")]
    ],
    resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Shashlik"),],
        [KeyboardButton(text="Ichimliklar 🥤"),KeyboardButton(text="Ikkinchi ovqatlar 🍛")],
        [KeyboardButton(text="ORQAGA ↩️")]
    ],
    resize_keyboard=True
)

shash = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text="Kuskavoy (mol go'shti)"),KeyboardButton(text="Kuskavoy (qo'y go'shti)")],
        [KeyboardButton(text="Rulet"),KeyboardButton(text="Napoleon")],
        [KeyboardButton(text="ORQAGA ↩️")]

    ],
    resize_keyboard=True
)

suv = ReplyKeyboardMarkup(
     keyboard=[
        [KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text="Coca-cola(0.5 l)"),KeyboardButton(text="Fanta(0.5 l)")],
        [KeyboardButton(text="Pepsi(1 l)"),KeyboardButton(text="bezgaz(1 l)")],
        [KeyboardButton(text="ORQAGA ↩️")]
    ],
    resize_keyboard=True
    
)

ikkinchiovqat = ReplyKeyboardMarkup(
       keyboard=[
        [KeyboardButton(text="Savatcha 🛒")],
        [KeyboardButton(text="Мясо по-гречески"),KeyboardButton(text="Мясо по-французски")],
        [KeyboardButton(text="Мишель"),KeyboardButton(text="Bifshtek")],
        [KeyboardButton(text="ORQAGA ↩️")]
    ],
    resize_keyboard=True

)
miqdr = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"),KeyboardButton(text="2"),KeyboardButton(text="3")],
        [KeyboardButton(text="4"),KeyboardButton(text="5"),KeyboardButton(text="6")],
        [KeyboardButton(text="7"),KeyboardButton(text="8"),KeyboardButton(text="9")],
        [KeyboardButton(text="ORQAGA ↩️")]
    ],
    resize_keyboard=True
)

