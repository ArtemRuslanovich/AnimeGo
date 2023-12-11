from bs4 import BeautifulSoup
from selenium import webdriver


async def search_parser(url : str):
    driver_path = r'D:\ХУЙНЯ\Utils\chromedriver\chromedriver.exe'  # замените это на путь к вашему драйверу

    # Запустите браузер
    driver = webdriver.Chrome(executable_path=driver_path)

    # Откройте страницу
    driver.get(url)

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
    print(href_list)
    
    # Закройте браузер
    driver.quit()

    return href_list