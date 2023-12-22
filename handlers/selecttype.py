from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from keyboards.type import type_keyboard
from aiogram.fsm.context import FSMContext
from utils.statesform import Selector

async def command_select_type_handler(message: Message, bot: Bot, state: FSMContext):
    await state.set_state(Selector.FIRST_CH)
    await message.reply(f"Время сделать выбор 🤔", reply_markup=type_keyboard)
