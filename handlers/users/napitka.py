from loader import dp
from aiogram import types
from states.state import kafe
from keyboards.default.kategorya import suv,miqdr
from aiogram.dispatcher import FSMContext
 

@dp.message_handler(text="Ichimliklar 🥤", state=kafe.category)
async def  bot_menu(message:types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat': cat}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=suv)
    await kafe.next()


@dp.message_handler(text="Coca-cola(0.5 l)", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()


@dp.message_handler(text="Fanta(0.5 l)", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()


@dp.message_handler(text="Pepsi(1 l)", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()


@dp.message_handler(text="bezgaz(1 l)", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()


