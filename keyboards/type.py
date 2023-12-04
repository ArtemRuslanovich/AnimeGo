from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

type_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Аниме'
        ),
        KeyboardButton(
            text='Фильм'
        ),
        KeyboardButton(
            text='Сериал'
        ),
        KeyboardButton(
            text='Мультик'
        ),
    ],
    [
        KeyboardButton(
            text='Не знаю'
        )
    ]
],
resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Время выбирать', selective=True
)