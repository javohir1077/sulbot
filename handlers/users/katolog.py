
from tkinter import Menu
from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.kategorya import menu
from states.state import kafe
 
@dp.message_handler(text="🛍️ Каталог")
async def  bot_menu(message:types.Message):
    await message.answer("Kategoriyani talang",reply_markup=menu)
    await kafe.category.set()

