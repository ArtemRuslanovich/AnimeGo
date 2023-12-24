from aiogram.enums import ParseMode
from urllib.parse import quote
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.clean_parsed_res import extract_anime_id
from utils.form.description_parser import description_parser
from utils.anime.search_parser import search_parser
from utils.statesform import Selector


async def select_manga(message: Message, state: FSMContext):
    await state.set_state(Selector.FIND_MANGA)
    await message.reply("Напиши что ты хочешь почитать, я постараюсь найти 🔍🔍🔍")

async def search_manga(message: Message, state: FSMContext):
    words = message.text.split()
    words_joined = " ".join(words)
    url = f"https://animego.org/search/manga?q={quote(words_joined)}"
    
    search_parsed_result = await search_parser(url)
    
    if search_parsed_result:
        parsed_result = search_parsed_result[0]
        clean_parsed_result = await extract_anime_id(parsed_result)
        
        async def send_description_message(parsed_result):
            poster_url, title, description, rating, anime_id = await description_parser(parsed_result)
            message_text = f"<b>{title}</b>\n\n" \
                           f"Рейтинг: {rating}\n" \
                           f"{description}\n" \
                           f"{parsed_result}"
            add_button = InlineKeyboardButton(text="Добавить в избранное", callback_data=f'add_{clean_parsed_result}')
            #good_image = improve_image_quality_with_api(poster_url)

            # Создаем клавиатуру и добавляем к ней кнопку
            key_add = InlineKeyboardMarkup(inline_keyboard=[[add_button]])
            await message.answer_photo(photo=poster_url, caption=message_text, parse_mode=ParseMode.HTML, reply_markup=key_add)

        await send_description_message(parsed_result)
    else:
        await message.answer("Ничего не найдено.")
    
    await state.clear()
    await state.set_state(Selector.FIRST_CH)

    