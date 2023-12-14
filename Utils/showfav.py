
import asyncio
import asyncpg


DATABASE_URL = "postgresql://postgres:80156120189fap@localhost/Users"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(connection):
    await connection.close()

async def show_fav_list(user_id: int):
    connection = await connect_to_db()
    try:
            # Получаем данные пользователя из базы данных
            user_data = await connection.fetchrow("Select anime_list from usersdata where user_id = $1", user_id)
            url = f"https://animego.org/anime/"
            anime_values = user_data["anime_list"] if user_data["anime_list"] else []
            def clean_anime_value(anime_value):
                return anime_value.replace('_', '-')

    # Iterate through each anime value and generate the URL
            anime_urls = [f"https://animego.org/anime/{clean_anime_value(anime)}" for anime in anime_values]

            return anime_urls



    finally:
        # Всегда закрывайте соединение, даже в случае ошибки
        await close_db_connection(connection)
