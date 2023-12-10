from bs4 import BeautifulSoup
#import requests
import random
import aiohttp


async def parser(url: str, num_links=5):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')

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
                random_links = random.sample(href_list, min(num_links, len(href_list)))
                return random_links