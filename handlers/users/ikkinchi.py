from loader import dp
from aiogram import types
from states.state import kafe
from keyboards.default.kategorya import ikkinchiovqat,miqdr
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="Ikkinchi ovqatlar 🍛", state=kafe.category)
async def  bot_menu(message:types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat': cat}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=ikkinchiovqat)
    await kafe.next()


@dp.message_handler(text="Мясо по-гречески", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()


@dp.message_handler(text="Мясо по-французски", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()

@dp.message_handler(text="Мишель", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()

@dp.message_handler(text="Bifshtek", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()
