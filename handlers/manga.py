from aiogram import Bot, types
from aiogram.enums import ParseMode
import pandas as pd
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from Utils.manga.manga_img import improve_image_quality_with_api
from Utils.statesform import Selector


async def select_manga(message: Message, bot: Bot, state: FSMContext):
    await state.set_state(Selector.FIND_MANGA)
    await message.reply("Напиши что ты хочешь почитать, я постараюсь найти 🔍🔍🔍")

async def search_manga_by_title(title_query, dataset_path='D:\ХУЙНЯ\MAL-manga.csv'):
    manga_dataset = pd.read_csv(dataset_path)
    title_query_lower = title_query.lower()
    manga_dataset['Title_lower'] = manga_dataset['Title'].str.lower()
    search_results = manga_dataset[manga_dataset['Title_lower'].str.contains(title_query_lower)]
    return search_results[['Title','Score', 'image_url']]

async def search_manga(message: types.Message, state: FSMContext):
    search_query = message.text
    results = await search_manga_by_title(search_query)

    if not results.empty:
        for index, row in results.iterrows():
            title = row['Title']
            score = row['Score']
            url_image = row['image_url']
            
            manga_info = f"<b>{title}</b>\n" \
                         f"Оценка: {score}\n"
            
            add_button = InlineKeyboardButton(text="Добавить в избранное", callback_data=f'add_{title}')
            #good_image = improve_image_quality_with_api(url_image)

            # Создаем клавиатуру и добавляем к ней кнопку
            key_add = InlineKeyboardMarkup(inline_keyboard=[[add_button]])
            await message.answer_photo(photo=url_image, caption=manga_info, parse_mode=ParseMode.HTML, reply_markup=key_add)
    else:
        search_results_text = f"Манга с названием '{search_query}' не найдена."
        await message.reply(search_results_text)

    await state.clear()
    await state.set_state(Selector.FIRST_CH)

    