from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_data import course_callback, book_callback
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, telegram_keyboard, algoritm_keyboard, booksMenu
from loader import dp


@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    await message.answer(f"Mahsulotni tanlang", reply_markup=categoryMenu)


@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kursni tanlang", reply_markup=coursesMenu)


@dp.callback_query_handler(text_contains="books")
async def buy_books(call: CallbackQuery):
    await call.message.answer("Kitoblar", reply_markup=booksMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel")
async def buy_courses(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()


@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buying_course(call: CallbackQuery, callback_date: dict):
    await call.message.answer(f"Siz mukammal Telegram bot kursini tanladingiz", reply_markup=telegram_keyboard)
    await call.answer(cache_time=20)


@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def buying_book(call: CallbackQuery, callback_date: dict):
    await call.answer("Buyurtmangiz qabul qilindi", show_alert=True)