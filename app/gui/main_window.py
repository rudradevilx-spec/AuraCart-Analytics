import customtkinter as ctk

from app.gui.scraper_tab import ScraperTab
from app.gui.analytics_tab import AnalyticsTab
from app.gui.settings_tab import SettingsTab

from app.database.postgres import db_manager


class AuraCartMainWindow:

    def __init__(self):

        ctk.set_appearance_mode(
            "dark"
        )

        ctk.set_default_color_theme(
            "blue"
        )

        self.root = ctk.CTk()

        self.root.title(
            "AuraCart Analytics Pro"
        )

        self.root.geometry(
            "1400x900"
        )

        self.root.minsize(
            1200,
            800
        )

        self.current_tab = None

        self.build_layout()

        self.show_scraper_tab()

    def build_layout(self):

        self.sidebar = ctk.CTkFrame(
            self.root,
            width=220,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.content_frame = ctk.CTkFrame(
            self.root
        )

        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.build_sidebar()

        self.build_status_bar()

    def build_sidebar(self):

        title = ctk.CTkLabel(
            self.sidebar,
            text="AuraCart",
            font=(
                "Segoe UI",
                28,
                "bold"
            )
        )

        title.pack(
            pady=(30, 20)
        )

        self.scraper_btn = ctk.CTkButton(
            self.sidebar,
            text="Scraper",
            command=self.show_scraper_tab
        )

        self.scraper_btn.pack(
            fill="x",
            padx=15,
            pady=10
        )

        self.analytics_btn = ctk.CTkButton(
            self.sidebar,
            text="Analytics",
            command=self.show_analytics_tab
        )

        self.analytics_btn.pack(
            fill="x",
            padx=15,
            pady=10
        )

        self.settings_btn = ctk.CTkButton(
            self.sidebar,
            text="Settings",
            command=self.show_settings_tab
        )

        self.settings_btn.pack(
            fill="x",
            padx=15,
            pady=10
        )

    def build_status_bar(self):

        self.status_frame = ctk.CTkFrame(
            self.root,
            height=35
        )

        self.status_frame.pack(
            side="bottom",
            fill="x"
        )

        db_status = (
            "Connected"
            if db_manager.health_check()
            else "Disconnected"
        )

        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text=(
                f"Database: {db_status}"
            )
        )

        self.status_label.pack(
            side="left",
            padx=10
        )

    def clear_content(self):

        for widget in (
            self.content_frame.winfo_children()
        ):
            widget.destroy()

    def show_scraper_tab(self):

        self.clear_content()

        self.current_tab = ScraperTab(
            self.content_frame
        )

        self.current_tab.pack(
            fill="both",
            expand=True
        )

    def show_analytics_tab(self):

        self.clear_content()

        self.current_tab = AnalyticsTab(
            self.content_frame
        )

        self.current_tab.pack(
            fill="both",
            expand=True
        )

    def show_settings_tab(self):

        self.clear_content()

        self.current_tab = SettingsTab(
            self.content_frame
        )

        self.current_tab.pack(
            fill="both",
            expand=True
        )

    def run(self):

        self.root.mainloop()