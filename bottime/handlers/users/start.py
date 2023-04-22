from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.tugma import menu

from loader import dp
from states.holat import holats
from aiogram.dispatcher import FSMContext



@dp.message_handler(CommandStart())
@dp.message_handler(CommandStart(), state=holats.kirit2)
@dp.message_handler(text="Asosiy menuga", state=holats.kirit3)
@dp.message_handler(text="Asosiy menuga")
@dp.message_handler(text="Asosiy menuga", state=holats.hajm)
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu)

