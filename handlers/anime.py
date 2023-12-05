from aiogram import Bot
from aiogram.types import Message
from urllib.parse import quote
from aiogram.fsm.context import FSMContext
from Utils.statesform import Selector
from Utils.form.parser import parser

async def select_anime(message: Message, bot: Bot, state: FSMContext):
    await state.set_state(Selector.FIND_ANIME)
    await message.reply("Отлично, у меня самого настроение японские мультики посмотреть...")

async def find_anime(message: Message, bot: Bot, state: FSMContext):
    words = message.text.split()
    
    words_joined = " ".join(words)
    
    url = f"https://animego.org/search/all?q={quote(words_joined)}"
    
    parsed_results = await parser(url)
    await message.answer(parsed_results[0])

    await state.clear()