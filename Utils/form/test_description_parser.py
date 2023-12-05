from bs4 import BeautifulSoup
import requests
import json


url = 'https://animego.org/anime/voshozhdenie-v-teni-2-2390'

# Отправляем запрос на сервер и получаем HTML-страницу
response = requests.get(url)
print(response.status_code)
html_code = response.text
soup = BeautifulSoup(html_code, 'html.parser')

# Получаем данные
poster_url = soup.find('meta', property='og:image')['content']

title = soup.find('title').text
cleaned_title = title.replace("смотреть онлайн — Аниме", "").strip()

description = soup.find('meta', {'name': 'description'})['content']

aggregate_rating_script = soup.find('script', {'type': 'application/ld+json'})
if aggregate_rating_script:
    json_data = json.loads(aggregate_rating_script.string)
    rating = json_data['aggregateRating']['ratingValue']

# Примеры для остальных данных, уточните селекторы в соответствии с вашим HTML-кодом
# rating = soup.find('ваш_селектор_рейтинга').text

# Выводим полученные данные
print("Постер:", poster_url)
print("Название:", cleaned_title)
print("Описание:", description)
print("Рейтинг:", rating)
