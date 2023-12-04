from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from keyboards.type import type_keyboard
from aiogram.fsm.context import FSMContext
from Utils.statesform import StatesForm

async def command_select_type_handler(message: Message, bot: Bot):
    await message.reply(f"Время сделать выбор", reply_markup=type_keyboard)
