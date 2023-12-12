from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

key_yes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Да',
            callback_data='Да'
        )
    ]
])
key_sub = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Подписаться',
            callback_data='Подписаться'
        )
    ]
])