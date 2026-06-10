import asyncio
import random
from typing import List

import aiohttp

from app.scraping.requests_scraper import (
    RequestsScraper
)

from app.utils.constants import (
    USER_AGENTS
)


class AsyncScraper:

    def __init__(self):

        self.parser = (
            RequestsScraper()
        )

    async def fetch(
        self,
        session,
        url
    ):

        headers = {
            "User-Agent":
            random.choice(
                USER_AGENTS
            )
        }

        try:

            async with session.get(
                url,
                headers=headers
            ) as response:

                response.raise_for_status()

                return (
                    await response.text()
                )

        except Exception:

            return None

    async def fetch_all(
        self,
        urls: List[str]
    ):

        async with aiohttp.ClientSession() as session:

            tasks = []

            for url in urls:

                tasks.append(
                    self.fetch(
                        session,
                        url
                    )
                )

            return await asyncio.gather(
                *tasks
            )

    async def scrape_urls(
        self,
        urls: List[str]
    ):

        html_pages = (
            await self.fetch_all(
                urls
            )
        )

        total_found = 0

        total_saved = 0

        all_products = []

        for url, html in zip(
            urls,
            html_pages
        ):

            if not html:

                continue

            products = (
                self.parser
                .parse_products(
                    html,
                    url
                )
            )

            saved = (
                self.parser
                .save_products(
                    products
                )
            )

            total_found += (
                len(products)
            )

            total_saved += saved

            all_products.extend(
                products
            )

        return {
            "success": True,
            "products_found":
            total_found,
            "products_saved":
            total_saved,
            "products":
            all_products
        }