from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from handlers.users import menustart
from keyboards.default import startMenuKeys
from keyboards.default.startMenuKeys import menuStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuStart)

