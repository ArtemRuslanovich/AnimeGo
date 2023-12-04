from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from Utils.statesform import StatesForm
from Utils.dbconnect import Request

async def command_start_handler(message: Message, bot: Bot, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await message.reply(f"Привет, {hbold(message.from_user.full_name)}! Начнем?")

async def command_help_handler(message: Message, bot: Bot) -> None:
    await message.reply(f"Этот бот предназначен для помощи с поиском нужного вам Аниме\Сериала\Фильма. Чтобы начать, напиши сообщение название и сезон. Например попробуй найти 'Магическая Битва 2 сезон'")


async def get_photo(message: Message, bot: Bot) -> None:
    await message.reply(f"Ого, фотокарточка. И что прикажешь с этим делать?")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, "D:\ХУЙНЯ\Насрали\photo.png")


#async def get_random_message(message: Message, bot: Bot) -> None:
#    url = f"https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
#   
#   await message.answer(f"Это спасет твою жизнь {url}")
