import threading
import time

import schedule

from app.scraping.requests_scraper import (
    RequestsScraper
)

from app.scraping.playwright_scraper import (
    PlaywrightScraper
)

from app.scraping.async_scraper import (
    AsyncScraper
)

import asyncio


class AuraScheduler:

    def __init__(self):

        self.requests_scraper = (
            RequestsScraper()
        )

        self.async_scraper = (
            AsyncScraper()
        )

        self.playwright_scraper = (
            PlaywrightScraper()
        )

        self.running = False

    def run_requests_job(
        self,
        url
    ):

        self.requests_scraper.scrape(
            url
        )

    def run_playwright_job(
        self,
        url
    ):

        self.playwright_scraper.scrape(
            url
        )

    def run_async_job(
        self,
        url
    ):

        asyncio.run(
            self.async_scraper.scrape_urls(
                [url]
            )
        )

    def schedule_requests(
        self,
        url,
        minutes
    ):

        schedule.every(
            minutes
        ).minutes.do(
            self.run_requests_job,
            url
        )

    def schedule_playwright(
        self,
        url,
        minutes
    ):

        schedule.every(
            minutes
        ).minutes.do(
            self.run_playwright_job,
            url
        )

    def schedule_async(
        self,
        url,
        minutes
    ):

        schedule.every(
            minutes
        ).minutes.do(
            self.run_async_job,
            url
        )

    def scheduler_loop(self):

        self.running = True

        while self.running:

            schedule.run_pending()

            time.sleep(1)

    def start(self):

        thread = threading.Thread(
            target=self.scheduler_loop,
            daemon=True
        )

        thread.start()

    def stop(self):

        self.running = False