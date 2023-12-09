from bs4 import BeautifulSoup
import requests
import random

url = 'https://animego.org/search/all?q=%D0%BC%D0%B0%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F+%D0%B1%D0%B8%D1%82%D0%B2%D0%B0+2'

# Отправляем запрос на сервер и получаем HTML-страницу
response = requests.get(url)
print(response.status_code)

# Проверяем успешность запроса
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)

    # Находим все элементы с классом 'col-12'
    items = soup.find_all('div', class_='col-12')

    # Создаем список для хранения ссылок
    href_list = []

    # Проходим по найденным элементам и извлекаем информацию
    for item in items:
        # Получаем ссылку
        link = item.find('a')
        if link:
            href_list.append(link['href'])

    # Выбираем случайные ссылки
    num_links = 5
    random_links = random.sample(href_list, min(num_links, len(href_list)))
    print(random_links)