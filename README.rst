.. image:: https://img.shields.io/pypi/pyversions/aiogram.svg?style=flat-square
    :target: https://pypi.python.org/pypi/aiogram
    :alt: Supported python versions

.. image:: https://img.shields.io/badge/dynamic/json?color=blue&logo=telegram&label=Telegram%20Bot%20API&query=%24.api.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Faiogram%2Faiogram%2Fdev-3.x%2F.butcher%2Fschema%2Fschema.json&style=flat-square
    :target: https://core.telegram.org/bots/api
    :alt: Telegram Bot API

Telegram Anime Recommendation Bot
=================================

Overview
--------

This Telegram bot is designed to assist users in discovering and managing their favorite anime and manga titles. It utilizes web scraping techniques with BeautifulSoup (BS4) and Selenium for data extraction, while storing information in a PostgreSQL database. The bot is built using the `aiogram <https://docs.aiogram.dev/>`_ framework, allowing for asynchronous interactions with Telegram's API. Additionally, `aiohttp`_ is employed to ensure smooth and efficient asynchronous communication.

Features
--------

1. **Anime and Manga Search:** Users can search for anime or manga titles based on their titles.

2. **Anime Recommendations:** The bot provides recommendations to help users choose which anime to watch.

3. **Favorite List:** Users can add anime or manga titles to their favorite list for easy access.

Installation
------------

1. Clone the repository::

   git clone https://github.com/ArtemRuslanovich/AnimeGo


2. Install requirements::
   
   ```pip install requirements.txt

3. Run app::
   
   ```python main.py
