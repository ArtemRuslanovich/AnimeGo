from urllib.parse import urlparse

async def extract_anime_id(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    anime_id = path.rsplit('/', 1)[-1]
    anime_id = anime_id.replace('-', '_') if anime_id else None
    return anime_id