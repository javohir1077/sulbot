from states.state import kafe
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp

from keyboards.default.kategorya import menu,shash,suv,ikkinchiovqat,miqdr,asosiy




@dp.message_handler(text="ORQAGA ↩️",state=kafe.category)
async def orqa1(message: types.Message, state: FSMContext):
    await message.answer("Davom etamizmi? 👨🏻‍🍳🔥",reply_markup=asosiy)
    await kafe.category.set()


@dp.message_handler(text="ORQAGA ↩️",state=kafe.category)
async def orqa1(message: types.Message, state: FSMContext):
    await message.answer(f"Sahifani tanlang 😊", reply_markup=asosiy)
    await state.finish()


@dp.message_handler(text="ORQAGA ↩️",state=kafe.product)
async def orqa1(message: types.Message, state: FSMContext):
    await message.answer("Xo'sh, buyurtmaga o'tamizmi, sizni issiq taomlarimiz kutmoqda 👨🏻‍🍳🔥",reply_markup=menu)
    await kafe.category.set()




@dp.message_handler(text="ORQAGA ↩️",state=kafe.amount)
async def orqa1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    cat = data.get('cat')
    if cat == 'Shashlik':
        await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", reply_markup=shash)
        await kafe.product.set()
    
    elif cat == 'Ikkinchi ovqatlar 🍛':
        await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=ikkinchiovqat)
        await kafe.product.set()
    
    elif cat == "Ichimliklar 🥤":
        await message.answer("<i>Batafsil ma'lumot uchun taomni tanlang</i>", parse_mode='html', reply_markup=suv)
        await kafe.product.set() 
    

  