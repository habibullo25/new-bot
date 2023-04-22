from loader import dp
import aiogram
from aiogram import types
from keyboards.default.tugma import tugma2
from keyboards.default.tugma import tugma3, tugma4, menu, tugma5
from aiogram.dispatcher import FSMContext
from states.holat import holats
from aiogram.dispatcher.filters.builtin import CommandStart

def volume_converter(volume, from_unit, to_unit):
    
    unit_factors = {
        'millimetr kub': 1,
        'santimetr kub': 1000,
        'detsimetr kub': 1000000,
        'metr kub': 1000000000,
        'litr': 1000000,
        'gektolitr': 100000,
        'yard kub': 764554858,
        'fut kub': 28316846.6,
    }

    volume_in_mm3 = volume * unit_factors[from_unit]

    converted_volume = volume_in_mm3 / unit_factors[to_unit]

    return converted_volume
   
@dp.message_handler(CommandStart(), state=holats.kirit2)
@dp.message_handler(text="Asosiy menuga", state=holats.kirit2)
@dp.message_handler(text="Asosiy menuga", state=holats.kirit3)
@dp.message_handler(text="Asosiy menuga", state=holats.hajm)
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu)
   
@dp.message_handler(aiogram.dispatcher.filters.Text(endswith='>>'), state=holats.hajm)
async def begin(message: types.Message, state: FSMContext):
    birlik = message.text[:-3]
    await state.update_data({"birlik1": birlik})
    await message.answer(text="Qiymat kiriting!")
    await holats.kirit2.set()
    
@dp.message_handler(state=holats.kirit2)
async def begin(message: types.Message, state: FSMContext):
    try:
        n = float(message.text)
        await state.update_data({"qiymat": n})
        await message.answer("O'tkaziluvchi birlikni tanlang!", reply_markup=tugma5)
        await holats.kirit3.set()
    except:
        await message.answer("Son qiymat kiritilmadi, iltimos son qiymat kiriting!")
        await holats.kirit2.set()

@dp.message_handler(state=holats.kirit3)
async def begin(message: types.Message, state: FSMContext):
    data = await state.get_data()
    birlik1 = data.get("birlik1")
    qiymat = data.get("qiymat")
    birlik2 = message.text[3:]
    natija = volume_converter(qiymat, birlik1, birlik2)
    if int(natija) == natija:
        natija = int(natija)
    if int(qiymat) == qiymat:
        qiymat = int(qiymat)
    await message.answer(f"{qiymat} {birlik1} = {str(natija)} {birlik2}", reply_markup=menu)
    await state.finish()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


def weight_converter(weight, from_unit, to_unit):
    unit_factors = {
        'gramm': 1,
        'kilogramm': 1000,
        'sentner': 100000,
        'tonna': 1000000,
        'funt': 453.592,
        'karat': 0.2,
    }

    weight_in_grams = weight * unit_factors[from_unit]

    converted_weight = weight_in_grams / unit_factors[to_unit]

    return converted_weight

@dp.message_handler(text="Og'irlik bilan ishlash")
async def begin(message: types.Message):
    await message.answer(text="Qaysi birlikni tanlaysiz?",reply_markup=tugma2)
    
@dp.message_handler(text="Hajm bilan ishlash")
async def begin(message: types.Message):
    await message.answer(text="Qaysi birlikni tanlaysiz?",reply_markup=tugma3)
    await holats.hajm.set()
    
@dp.message_handler(aiogram.dispatcher.filters.Text(endswith='>>'))
async def begin(message: types.Message, state: FSMContext):
    birlik = message.text[:-3]
    await state.update_data({"birlik1": birlik})
    await message.answer(text="Qiymat kiriting!")
    await holats.kirit.set()
    
@dp.message_handler(state=holats.kirit)
async def begin(message: types.Message, state: FSMContext):
    try:
        n = float(message.text)
        await state.update_data({"qiymat": n})
        await message.answer("O'tkaziluvchi birlikni tanlang!", reply_markup=tugma4)
        await holats.kirit1.set()
    except:
        await message.answer("Son qiymat kiritilmadi, iltimos son qiymat kiriting!")

@dp.message_handler(state=holats.kirit1)
async def begin(message: types.Message, state: FSMContext):
    data = await state.get_data()
    birlik1 = data.get("birlik1")
    qiymat = data.get("qiymat")
    birlik2 = message.text[3:]
    natija = weight_converter(qiymat, birlik1, birlik2)
    if int(natija) == natija:
        natija = int(natija)
    if int(qiymat) == qiymat:
        qiymat = int(qiymat)
    await message.answer(f"{qiymat} {birlik1} = {str(natija)} {birlik2}", reply_markup=menu)
    await state.finish()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        

