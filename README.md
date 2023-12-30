


# Telegram Anime Recommendation Bot

.. image:: https://img.shields.io/pypi/pyversions/aiogram.svg?style=flat-square
    :target: https://pypi.python.org/pypi/aiogram
    :alt: Supported python versions

.. image:: https://img.shields.io/badge/dynamic/json?color=blue&logo=telegram&label=Telegram%20Bot%20API&query=%24.api.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Faiogram%2Faiogram%2Fdev-3.x%2F.butcher%2Fschema%2Fschema.json&style=flat-square
    :target: https://core.telegram.org/bots/api
    :alt: Telegram Bot API

**Telegram bot** that provides anime and manga recommendations, allows users to search by title, and manage a favorites list. The bot is built using **aiogram**, utilizes web scraping with **Beautiful Soup (BS4)** and **Selenium**, and stores data in a **PostgreSQL** database.

## Features

1. **Anime Search by Title:** Users can search for anime or manga by title to get detailed information.

2. **Anime Recommendations:** The bot helps users choose anime or manga to watch based on preferences.

3. **Favorites List:** Users can add anime or manga to their favorites list for future reference.

## Technologies Used

- **aiogram:** The bot framework used for interaction with the Telegram API.
- **aiohttp:** Enables asynchronous HTTP requests for better performance.
- **Beautiful Soup (BS4):** For web scraping anime/manga details.
- **Selenium:** Used in conjunction with BS4 for scenarios where dynamic content requires JavaScript rendering.
- **PostgreSQL:** The chosen database for storing user data and favorites.

## Getting Started

### Prerequisites

1. Python 3.7 or higher
2. PostgreSQL installed and configured

### Installation

1. **Clone the repository:**

   ```bash
   git clone hhttps://github.com/ArtemRuslanovich/AnimeGo

2. **INSTALL REQUIREMENTS:**

   ```bash
   pip install -r requirements.txt

3. **RUN APPLICATION:**

   ```bash
   python main.py