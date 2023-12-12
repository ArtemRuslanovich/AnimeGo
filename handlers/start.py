from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from Utils.statesform import Selector
from Utils.dbconnect import Request
from keyboards.inline import key_yes
from aiogram.fsm.context import FSMContext
from keyboards.type import type_keyboard


async def command_start_handler(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await message.reply(f"Привет, {hbold(message.from_user.full_name)}! Начнем?", reply_markup=key_yes)

async def command_help_handler(message: Message, bot: Bot) -> None:
    await message.reply(f"Этот бот предназначен для помощи с поиском нужного вам Аниме.")

async def command_back_handler(message: Message, bot: Bot, state: FSMContext) -> None:
    state.set_state(Selector.FIRST_CH)
    await message.reply(f"Время сделать выбор", reply_markup=type_keyboard)

async def get_photo(message: Message, bot: Bot) -> None:
    await message.reply(f"Ого, фотокарточка. Пошел нахуй")
