from aiogram import Bot
from aiogram.types import Message
from urllib.parse import quote
from aiogram.fsm.context import FSMContext
from Utils.statesform import Selector

async def select_film(message: Message, bot: Bot, state: FSMContext):
    await state.set_state(Selector.FIND_FILM)
    await message.reply("Супер, как на счет Муви43?))))")

async def find_film(message: Message, bot: Bot, state: FSMContext):
    words = message.text.split()
    
    words_joined = " ".join(words)
    
    url = f"https://www.kinopoisk.ru/index.php?kp_query={quote(words_joined)}"
    
    await message.answer(f"Что удалось найти: {url}")

    await state.clear()