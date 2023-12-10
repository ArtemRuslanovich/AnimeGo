from bs4 import BeautifulSoup
import aiohttp
#import requests
import json

async def description_parser(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                html_content = await response.text()
                soup = BeautifulSoup(html_content, 'html.parser')

                poster_url = soup.find('meta', property='og:image')['content']
                title = soup.find('title').text
                cleaned_title = title.replace("смотреть онлайн — Аниме", "").strip()

                description = soup.find('meta', {'name': 'description'})['content']
                cleaned_description = description.replace("Смотреть онлайн аниме", "").strip()

                aggregate_rating_script = soup.find('script', {'type': 'application/ld+json'})
                rating = None
                if aggregate_rating_script:
                    json_data = json.loads(aggregate_rating_script.string)
                    rating = json_data['aggregateRating']['ratingValue']

                return poster_url, cleaned_title, cleaned_description, rating
