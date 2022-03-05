from loader import dp
from aiogram import types
from states.state import kafe
from keyboards.default.kategorya import shash,miqdr
from aiogram.dispatcher import FSMContext
 

@dp.message_handler(text="Shashlik", state=kafe.category)
async def  bot_menu(message:types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat': cat}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=shash)
    await kafe.next()


@dp.message_handler(text="Kuskavoy (mol go'shti)", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()


@dp.message_handler(text="Kuskavoy (qo'y go'shti)", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()


@dp.message_handler(text="Rulet", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()


@dp.message_handler(text="Napoleon", state=kafe.product)
async def  bot_menu(message:types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'odi': name}
    )
    await message.answer("kategoriyalarni tanlang",reply_markup=miqdr)
    await kafe.next()