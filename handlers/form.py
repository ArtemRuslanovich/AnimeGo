from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from keyboards.genres import genres_keyboard
from aiogram.fsm.context import FSMContext
from Utils.statesform import StatesForm
from Utils.form.parser import parser
from Utils.form.description_parser import description_parser
from aiogram.enums import ParseMode
import datetime
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



async def command_select_genre_handler(message: Message, state: FSMContext):
    await message.answer(f"Ну ладно {message.from_user.first_name}, давай начем с простого. Для начала укажи, на какой жанр у тебя сегодня настроение", reply_markup=genres_keyboard)
    await state.set_state(StatesForm.GET_GENRE)

async def command_select_year_handler(message: Message, bot: Bot, state: FSMContext):
    await message.reply(f"Хорошо, напиши мне год выхода фильма. Если не знаешь - напиши любой, который первый попадется в голову")
    await state.update_data(genre=message.text)
    await state.set_state(StatesForm.GET_YEAR)

async def command_show_examples(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(year=message.text)
    data = await state.get_data()
    genre = data["genre"]
    year = int(data["year"])
    if 1900 <= year <= datetime.datetime.now().year + 1:
        await message.reply(f'работает жанр {genre}, год {year}')

        url = f"https://animego.org/anime/filter/year-from-{year}/genres-is-{genre}/apply"
        parsed_results = await parser(url)
        async def send_description_message(parsed_result):
            poster_url, title, description, rating, anime_id = await description_parser(parsed_result)
            message_text = f"<b>{title}</b>\n\n" \
                        f"Рейтинг: {rating}\n" \
                        f"{description}\n" \
                        f"{parsed_result}"
            subscribe_button = InlineKeyboardButton(text="Подписаться", callback_data=f'subscribe_{anime_id}')

    # Создаем клавиатуру и добавляем к ней кнопку
            key_sub = InlineKeyboardMarkup(inline_keyboard=[[subscribe_button]])
            await message.answer_photo(photo=poster_url, caption=message_text, parse_mode=ParseMode.HTML, reply_markup=key_sub)


        # Используем цикл для отправки сообщений на основе данных из description_parser
        for parsed_result in parsed_results[:5]:  # Первые 5 результатов, можно изменить по необходимости
            await send_description_message(parsed_result)
    
        await state.clear()
        await state.set_state(StatesForm.GET_GENRE)
    else:
        await message.answer("Аниме в данном году не найдено")
        await state.clear()
        await state.set_state(StatesForm.GET_YEAR)