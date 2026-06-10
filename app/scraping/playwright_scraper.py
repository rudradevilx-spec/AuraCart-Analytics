from playwright.sync_api import sync_playwright

from app.scraping.requests_scraper import (
    RequestsScraper
)


class PlaywrightScraper:

    def __init__(self):

        self.parser = (
            RequestsScraper()
        )

    def scrape(
        self,
        url
    ):

        browser = None

        try:

            with sync_playwright() as p:

                browser = (
                    p.chromium.launch(
                        headless=True
                    )
                )

                page = (
                    browser.new_page()
                )

                page.goto(
                    url,
                    timeout=60000
                )

                page.wait_for_timeout(
                    3000
                )

                html = page.content()

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

                return {
                    "success": True,
                    "products_found":
                    len(products),
                    "products_saved":
                    saved,
                    "products":
                    products
                }

        except Exception as error:

            return {
                "success": False,
                "error": str(error)
            }

        finally:

            if browser:

                browser.close()