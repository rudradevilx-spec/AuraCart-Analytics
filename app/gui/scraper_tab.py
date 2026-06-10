import customtkinter as ctk
import threading
import asyncio

from app.scraping.requests_scraper import RequestsScraper
from app.scraping.async_scraper import AsyncScraper
from app.scraping.playwright_scraper import PlaywrightScraper


class ScraperTab(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        # Scrapers
        self.requests_scraper = RequestsScraper()
        self.async_scraper = AsyncScraper()
        self.playwright_scraper = PlaywrightScraper()

        self.build_ui()

    # ---------------- UI ---------------- #

    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Scraper Engine",
            font=("Segoe UI", 26, "bold")
        )

        title.pack(pady=20, anchor="w", padx=20)

        # URL entry
        self.url_entry = ctk.CTkEntry(
            self,
            width=600,
            placeholder_text="Enter product URL"
        )

        self.url_entry.pack(padx=20, pady=10, anchor="w")

        # Mode selector
        self.mode = ctk.StringVar(value="requests")

        self.mode_frame = ctk.CTkFrame(self)
        self.mode_frame.pack(padx=20, pady=10, anchor="w", fill="x")

        ctk.CTkRadioButton(
            self.mode_frame,
            text="Requests",
            variable=self.mode,
            value="requests"
        ).pack(side="left", padx=10)

        ctk.CTkRadioButton(
            self.mode_frame,
            text="Async",
            variable=self.mode,
            value="async"
        ).pack(side="left", padx=10)

        ctk.CTkRadioButton(
            self.mode_frame,
            text="Playwright",
            variable=self.mode,
            value="playwright"
        ).pack(side="left", padx=10)

        # Button
        self.start_btn = ctk.CTkButton(
            self,
            text="Start Scraping",
            command=self.start_scraping
        )

        self.start_btn.pack(padx=20, pady=10, anchor="w")

        # Progress
        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(padx=20, pady=10, fill="x")
        self.progress.set(0)

        # Output box
        self.output = ctk.CTkTextbox(self, height=300)
        self.output.pack(padx=20, pady=10, fill="both", expand=True)

    # ---------------- SAFE UI UPDATE ---------------- #

    def log(self, message):

        self.after(
            0,
            lambda: self.output.insert("end", message + "\n")
        )

    def set_progress(self, value):

        self.after(
            0,
            lambda: self.progress.set(value)
        )

    def disable_button(self):

        self.after(
            0,
            lambda: self.start_btn.configure(state="disabled")
        )

    def enable_button(self):

        self.after(
            0,
            lambda: self.start_btn.configure(state="normal")
        )

    # ---------------- SCRAPING ENTRY ---------------- #

    def start_scraping(self):

        url = self.url_entry.get().strip()

        if not url:

            self.log("❌ Please enter a URL")
            return

        self.disable_button()

        self.log(f"Mode: {self.mode.get()}")
        self.log(f"Starting scrape: {url}")

        thread = threading.Thread(
            target=self.run_scraper,
            args=(url,),
            daemon=True
        )

        thread.start()

    # ---------------- WORKER THREAD ---------------- #

    def run_scraper(self, url):

        try:

            mode = self.mode.get()

            self.set_progress(0.2)

            if mode == "requests":

                result = self.requests_scraper.scrape(url)

            elif mode == "async":

                result = asyncio.run(
                    self.async_scraper.scrape_urls([url])
                )

            elif mode == "playwright":

                result = self.playwright_scraper.scrape(url)

            else:

                result = {"error": "Invalid mode"}

            self.set_progress(1.0)

            self.log(f"Done: {result}")

        except Exception as e:

            self.log(f"Error: {str(e)}")

        finally:

            self.enable_button()