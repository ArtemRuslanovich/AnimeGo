from bs4 import BeautifulSoup
import aiohttp
#import requests
import json
import re

async def description_parser(url: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Проверка на ошибку при запросе

                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')

                # Получаем значения с учетом возможных отсутствующих элементов
                poster_url = soup.find('meta', property='og:image')['content'] if soup.find('meta', property='og:image') else None
                title = soup.find('title').text.strip() if soup.find('title') else None
                description = soup.find('meta', {'name': 'description'})['content'].strip() if soup.find('meta', {'name': 'description'}) else None

                # Извлекаем идентификатор из URL с использованием регулярного выражения
                anime_id_match = re.search(r'\d+$', url)
                anime_id = anime_id_match.group() if anime_id_match else None

                aggregate_rating_script = soup.find('script', {'type': 'application/ld+json'})
                rating = None
                if aggregate_rating_script:
                    json_data = json.loads(aggregate_rating_script.string)
                    rating = json_data['aggregateRating']['ratingValue'] if 'aggregateRating' in json_data and 'ratingValue' in json_data['aggregateRating'] else None

                return poster_url, title, description, rating, anime_id
    except (aiohttp.ClientError, aiohttp.ClientResponseError) as e:
        print(f"Error during HTTP request: {e}")
        return None, None, None, None, None
