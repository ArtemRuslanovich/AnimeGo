from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from utils.clean_parsed_res import extract_anime_id
from utils.form.description_parser import description_parser
from utils.showfav import show_fav_list
from utils.statesform import Selector
from utils.dbconnect import Request
from keyboards.inline import key_yes
from aiogram.fsm.context import FSMContext
from keyboards.type import type_keyboard
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def command_start_handler(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await message.reply(f"Привет, {hbold(message.from_user.full_name)}! Начнем? 🙃", reply_markup=key_yes)

async def command_help_handler(message: Message, bot: Bot) -> None:
    await message.reply(f"Этот бот предназначен для помощи с поиском нужного вам Аниме.")

async def command_back_handler(message: Message, bot: Bot, state: FSMContext) -> None:
    await state.set_state(Selector.FIRST_CH)
    await message.reply(f"Время сделать выбор 🤔", reply_markup=type_keyboard)

async def command_fav_handler(message: Message, bot: Bot, state: FSMContext) -> None:
    user_id = message.from_user.id
    anime_urls = await show_fav_list(user_id)
    async def send_description_message(parsed_result):
            poster_url, title, description, rating, anime_id = await description_parser(parsed_result)
            message_text = f"<b>{title}</b>\n\n" \
                        f"Рейтинг: {rating}\n" \
                        f"{description}\n" \
                        f"{parsed_result}"
            subscribe_button = InlineKeyboardButton(text="Вы подписаны ✅", callback_data=f'subscribe_{clean_parsed_result}')

    # Создаем клавиатуру и добавляем к ней кнопку
            key_sub = InlineKeyboardMarkup(inline_keyboard=[[subscribe_button]])
            await message.answer_photo(photo=poster_url, caption=message_text, parse_mode=ParseMode.HTML, reply_markup=key_sub)


        # Используем цикл для отправки сообщений на основе данных из description_parser
    for parsed_result in anime_urls[:]:  # Первые 5 результатов, можно изменить по необходимости
        clean_parsed_result = await extract_anime_id(parsed_result)
        await send_description_message(parsed_result)

async def get_photo(message: Message, bot: Bot) -> None:
    await message.reply(f"Ого, фотокарточка. Пошел нахуй")
