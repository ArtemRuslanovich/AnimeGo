from aiogram.types import CallbackQuery
#from aiogram import Bot
from aiogram.fsm.context import FSMContext
from Utils.statesform import Selector
from keyboards.type import type_keyboard

async def handle_yes_callback(callback: CallbackQuery,state: FSMContext):
    state.set_state(Selector.FIRST_CH)
    await callback.message.answer(f"Время сделать выбор", reply_markup=type_keyboard)
    await callback.answer()

async def handle_sub_callback(callback: CallbackQuery,state: FSMContext):
    await callback.message.answer(f"Функция 'подписаться' пока не работает")
    await callback.answer()

