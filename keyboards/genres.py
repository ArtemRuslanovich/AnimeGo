from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

genres_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='horror🫣'
        ),
        KeyboardButton(
            text='comedy😂'
        ),
        KeyboardButton(
            text='thriller🤫'
        )
    ],
    [
        KeyboardButton(
            text='sci-fi🤖'
        ),
        KeyboardButton(
            text='historical'
        ),
        KeyboardButton(
            text='action💥'
        )
    ],
    [
        KeyboardButton(
            text='family👨‍👩‍👧‍👦'
        ),
        KeyboardButton(
            text='drama😭'
        ),
        KeyboardButton(
            text='parody🤡'
        )
    ],
],
resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Ну ДАВАЙ ДАВАЙ выбирай', selective=True
)