from selenium import webdriver
from bs4 import BeautifulSoup
import requests


driver_path = r'D:\ХУЙНЯ\Utils\chromedriver\chromedriver.exe'  # замените это на путь к вашему драйверу

    # Запустите браузер
driver = webdriver.Chrome(executable_path=driver_path)

    # Откройте страницу
driver.get("https://animego.org/search/all?q=%D0%BC%D0%B0%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F+%D0%B1%D0%B8%D1%82%D0%B2%D0%B0+2")

    # Дождитесь выполнения JavaScript на странице (может потребоваться настроить для вашего случая)
#driver.implicitly_wait(5)

    # Получите HTML-код страницы
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

        # Находим все элементы с классом 'col-12'
items = soup.find_all('div', class_='h5 font-weight-normal mb-2 card-title text-truncate')

        # Создаем список для хранения ссылок
href_list = []

        # Проходим по найденным элементам и извлекаем информацию
for item in items:
            # Получаем ссылку
    link = item.find('a')
    if link:
        href_list.append(link['href'])
print(href_list[0])

parsed_res=href_list

    
    # Закройте браузер
driver.quit()