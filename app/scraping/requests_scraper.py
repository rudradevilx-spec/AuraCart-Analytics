import random
import time
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from app.database.repository import ProductRepository
from app.scraping.proxy_manager import ProxyManager
from app.scraping.site_profiles import GenericProfile

from app.utils.constants import (
    USER_AGENTS,
    MAX_RETRIES,
    DEFAULT_TIMEOUT,
    RETRY_DELAY
)

from app.utils.logger import (
    AuraLogger
)


class RequestsScraper:



    def __init__(self):

        self.repository = ProductRepository()

        self.proxy_manager = ProxyManager()

        self.logger = AuraLogger.get_logger()

    def fetch_page(self, url: str) -> str:
        
        self.logger.info(
            f"Fetching URL: {url}"
        )

        self.logger.info(
            f"Fetched URL successfully: {url}"
        )
        
        self.logger.error(
            f"Request failed: {error}"
        )
        last_error = None

        for attempt in range(
            self.MAX_RETRIES
        ):

            try:

                headers = {
                    "User-Agent": random.choice(
                        self.USER_AGENTS
                    )
                }

                response = requests.get(
                    url=url,
                    headers=headers,
                    proxies=self.proxy_manager.get_requests_proxy(),
                    timeout=DEFAULT_TIMEOUT
                )

                response.raise_for_status()

                return response.text

            except RequestException as error:

                last_error = error

            time.sleep(
                self.RETRY_DELAY
        )

        raise RuntimeError(
            f"Failed to fetch page: {last_error}"
        )

    def _extract_text(
        self,
        product_card,
        selectors: List[str],
        default: str = "N/A"
    ) -> str:

        try:

            for selector in selectors:

                element = product_card.select_one(
                    selector
                )

                if element:

                    text = (
                        element.get_text(
                            strip=True
                        )
                    )

                    if text:

                        return text

            return default

        except Exception:

            return default

    def parse_products(
        self,
        html: str,
        source_url: str
    ) -> List[Dict]:

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        product_cards = (
            GenericProfile.detect_products(
                soup
            )
        )

        products = []

        for card in product_cards:

            try:

                name = self._extract_text(
                    card,
                    GenericProfile.NAME_SELECTORS
                )

                price = self._extract_text(
                    card,
                    GenericProfile.PRICE_SELECTORS
                )

                rating = self._extract_text(
                    card,
                    GenericProfile.RATING_SELECTORS
                )

                availability = self._extract_text(
                    card,
                    GenericProfile.AVAILABILITY_SELECTORS
                )

                if name == "N/A":

                    continue

                product = {
                    "name": name,
                    "price": price,
                    "rating": rating,
                    "availability": availability,
                    "source_url": source_url
                }

                products.append(
                    product
                )

            except Exception:

                continue

        return products

    def save_products(
        self,
        products: List[Dict]
    ) -> int:
        self.logger.info(
            f"Saved product: "
            f"{product['name']}"
        )
        
        self.logger.error(
            f"Save failed: {error}"
        )
        saved_count = 0

        for product in products:

            try:

                self.repository.add_product(
                    name=product["name"],
                    price=product["price"],
                    rating=product["rating"],
                    availability=product[
                        "availability"
                    ],
                    source_url=product[
                        "source_url"
                    ]
                )

                saved_count += 1

            except Exception:

                continue

        return saved_count

    def scrape(
        self,
        url: str
    ) -> Dict:

        try:

            html = self.fetch_page(
                url
            )

            products = self.parse_products(
                html,
                url
            )

            saved_count = (
                self.save_products(
                    products
                )
            )

            return {
                "success": True,
                "url": url,
                "products_found": len(
                    products
                ),
                "products_saved": saved_count,
                "products": products
            }

        except Exception as error:

            return {
                "success": False,
                "url": url,
                "products_found": 0,
                "products_saved": 0,
                "error": str(error)
            }