from bs4 import BeautifulSoup
import requests
import json

async def description_parser(url : str):
    
    # Отправляем запрос на сервер и получаем HTML-страницу
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        poster_url = soup.find('meta', property='og:image')['content']
        title = soup.find('title').text
        cleaned_title = title.replace("смотреть онлайн — Аниме", "").strip()

        description = soup.find('meta', {'name': 'description'})['content']
        cleaned_description = description.replace("Смотреть онлайн аниме", "").strip()

        aggregate_rating_script = soup.find('script', {'type': 'application/ld+json'})
        if aggregate_rating_script:
            json_data = json.loads(aggregate_rating_script.string)
            rating = json_data['aggregateRating']['ratingValue']

        # Выводим полученные данные
        return poster_url, cleaned_title, cleaned_description, rating
