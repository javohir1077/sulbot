from aiogram import types
from keyboards.default.kategorya import shash,suv,ikkinchiovqat
from loader import dp, db
from aiogram.dispatcher import FSMContext
from states.state import kafe
from handlers.users.narx import price



def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@dp.message_handler(state=kafe.amount)
async def orqa1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        od = data.get('odi')
        cat = data.get('cat')
        # nn = price[od]* int(n)
        if cat == 'Shashlik':
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=shash)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            
            await kafe.product.set()
        


        
        elif cat == "Ichimliklar 🥤":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=suv)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await kafe.product.set()
        elif cat == "Ikkinchi ovqatlar 🍛":
            await message.answer(f"{od} <i>dan {n} ta, Savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=ikkinchiovqat)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await kafe.product.set()
        else:
            await message.answer('Kategoriya saqlanmagan')
    else:
        await message.answer("Faqat son kiriting!")
        await kafe.amount.set()