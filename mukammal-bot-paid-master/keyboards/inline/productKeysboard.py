from aiogram.types import KeyboardButton, InlineKeyboardMarkup
categoryMemu = InlineKeyboardMarkup(
    inline_keyboard=[
            [InlineKeyboardMarkup(text="kurslar", callback_data="courses"),
             InlineKeyboardMarkup(text="kitoblar", callback_data="books"),
             ],
            [
                InlineKeyboardMarkup(text="link", url="https://t.me/shahzod"),
             ],
            [
                InlineKeyboardMarkup(text="qidirish", switch_inline_query_current_chat=" "),
            ],
            [
                InlineKeyboardMarkup(text="ulashish", switch_inline_query="jhf vjgbn")

            ],
    ]
)