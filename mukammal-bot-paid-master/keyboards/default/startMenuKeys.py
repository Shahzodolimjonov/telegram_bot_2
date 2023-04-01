from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulotlar"),
            KeyboardButton(text="o'quv markazlar"),
            KeyboardButton(text="fanlar"),
        ],

        [

            KeyboardButton(text="location", request_location=True),
            KeyboardButton(text="contact", request_contact=True),

        ],

    ],

    resize_keyboard=True

)