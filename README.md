# Telegram Anime Recommendation Bot

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
