from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from keyboards.genres import genres_keyboard
from aiogram.fsm.context import FSMContext
from Utils.statesform import StatesForm
from Utils.parser import parser

async def command_select_genre_handler(message: Message, state: FSMContext):
    await message.answer(f"Ну ладно {message.from_user.first_name}, давай начем с простого.  Для начала укажи, на какой жанр у тебя сегодня настроение", reply_markup=genres_keyboard)
    await state.set_state(StatesForm.GET_GENRE)

async def command_select_year_handler(message: Message, bot: Bot, state: FSMContext):
    await message.reply(f"Хорошо, напиши мне год выхода фильма. Если не знаешь - напиши любой, который первый попадется в голову")
    await state.update_data(genre=message.text)
    await state.set_state(StatesForm.GET_YEAR)

async def command_show_examples(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(year=message.text)
    data = await state.get_data()
    genre = data["genre"]
    year = data["year"]
    await message.reply(f'работает жанр {genre}, год {year}')

    url = f"https://animego.org/anime/filter/year-from-{year}/genres-is-{genre}/apply"
    await message.answer(url)
    parsed_results = await parser(url)
    await message.answer(parsed_results[0])
    await message.answer(parsed_results[1])
    await message.answer(parsed_results[2])
    await message.answer(parsed_results[3])
    await message.answer(parsed_results[4])
    await state.clear()
    await state.set_state(StatesForm.GET_GENRE)