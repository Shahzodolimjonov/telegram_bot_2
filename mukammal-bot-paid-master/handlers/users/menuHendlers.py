import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startMenuKeys import menuStart
from loader import dp


@dp.message_handler(text="o'quv markaz")
async def fanlar(message: types.Message):
    await message.answer(" PDP, Najot talim, GITA")

@dp.message_handler(text="fanlar")
async def Kurs_narxlari(message: types.Message):
    await message.answer("IELTS,Python,Java,C++,GO")


@dp.message_handler(content_types='contact')
async def contact(message: types.Message):
    await message.answer("Raqamingiz qabul qilindi")



@dp.message_handler(content_types="location")
async def location(message: types.Message):
    lat = message.location.latitude
    long = message.location.longitude
    await message.answer(f"{long},{lat}")
    await message.reply_location(latitude=lat, longitude=long)

