import asyncio

from app.scraping.async_scraper import (
    AsyncScraper
)

scraper = AsyncScraper()

urls = [
    "https://amazon.com",
    "https://flipkart.com"
]

result = asyncio.run(
    scraper.scrape_urls(
        urls
    )
)

print(result)