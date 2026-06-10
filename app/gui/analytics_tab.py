import customtkinter as ctk

from app.analytics.statistics import (
    StatisticsEngine
)

from app.analytics.charts import (
    ChartGenerator
)

from app.database.repository import (
    SessionRepository
)

from app.exports.csv_exporter import (
    CSVExporter
)

from app.exports.excel_exporter import (
    ExcelExporter
)

from app.exports.json_exporter import (
    JSONExporter
)
class AnalyticsTab(ctk.CTkFrame):

    def __init__(self, parent):

        self.statistics = StatisticsEngine()

        self.chart_generator = ChartGenerator()

        self.session_repo = SessionRepository()
        
        super().__init__(parent)

        self.product_repo = ProductRepository()

        self.session_repo = SessionRepository()

        self.build_ui()

        self.load_stats()

        self.load_statistics()
    def build_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Analytics Dashboard",
            font=("Segoe UI", 26, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        self.cards_frame = ctk.CTkFrame(
            self
        )

        self.cards_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.products_card = ctk.CTkFrame(
            self.cards_frame
        )

        self.products_card.pack(
            side="left",
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

        self.sessions_card = ctk.CTkFrame(
            self.cards_frame
        )

        self.sessions_card.pack(
            side="left",
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

        self.products_title = ctk.CTkLabel(
            self.products_card,
            text="Total Products"
        )

        self.products_title.pack(
            pady=(20, 5)
        )

        self.products_value = ctk.CTkLabel(
            self.products_card,
            text="0",
            font=("Segoe UI", 28, "bold")
        )

        self.products_value.pack(
            pady=(0, 20)
        )

        self.sessions_title = ctk.CTkLabel(
            self.sessions_card,
            text="Total Sessions"
        )

        self.sessions_title.pack(
            pady=(20, 5)
        )

        self.sessions_value = ctk.CTkLabel(
            self.sessions_card,
            text="0",
            font=("Segoe UI", 28, "bold")
        )

        self.sessions_value.pack(
            pady=(0, 20)
        )

        self.refresh_button = ctk.CTkButton(
            self,
            text="Refresh Statistics",
            command=self.load_stats
        )

        self.refresh_button.pack(
            padx=20,
            pady=20,
            anchor="w"
        )
        title = ctk.CTkLabel(
            self,
            text="Analytics Dashboard",
            font=("Segoe UI", 26, "bold")
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=20
        )
        
        self.metrics_frame = ctk.CTkFrame(
            self
        )

        self.metrics_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )
        
        self.products_label = ctk.CTkLabel(
            self.metrics_frame,
            text="Products: 0",
            font=("Segoe UI", 18)
        )

        self.products_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )
        self.sessions_label = ctk.CTkLabel(
            self.metrics_frame,
            text="Sessions: 0",
            font=("Segoe UI", 18)
        )

        self.sessions_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )
        
        self.price_label = ctk.CTkLabel(
            self.metrics_frame,
            text="Average Price: 0",
            font=("Segoe UI", 18)
        )

        self.price_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )
        
        self.rating_label = ctk.CTkLabel(
            self.metrics_frame,
            text="Average Rating: 0",
            font=("Segoe UI", 18)
        )

        self.rating_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )
        
        self.availability_box = ctk.CTkTextbox(
            self,
            height=200
        )

        self.availability_box.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.refresh_button = ctk.CTkButton(
            self,
            text="Refresh Analytics",
            command=self.load_statistics
        )

        self.refresh_button.pack(
            padx=20,
            pady=10,
            anchor="w"
        )

        self.chart_button = ctk.CTkButton(
            self,
            text="Show Availability Chart",
            command=self.show_chart
        )

        self.chart_button.pack(
            padx=20,
            pady=10,
            anchor="w"
        )
    def load_statistics(self):

        try:

            total_products = (
                self.statistics
                .total_products()
            )

            total_sessions = (
                self.session_repo
                .total_sessions()
            )

            average_price = (
                self.statistics
                .average_price()
            )

            average_rating = (
                self.statistics
                .average_rating()
            )

            availability = (
                self.statistics
                .availability_breakdown()
            )

            self.products_label.configure(
                text=f"Products: {total_products}"
            )

            self.sessions_label.configure(
                text=f"Sessions: {total_sessions}"
            )

            self.price_label.configure(
                text=f"Average Price: {average_price}"
            )

            self.rating_label.configure(
                text=f"Average Rating: {average_rating}"
            )

            self.availability_box.delete(
                "1.0",
                "end"
            )

            for key, value in (
                availability.items()
            ):

                self.availability_box.insert(
                    "end",
                    f"{key}: {value}\n"
                )

        except Exception as error:

            print(
                f"Analytics Error: {error}"
            )
    def show_chart(self):

        self.chart_generator.availability_chart()
    
    def load_stats(self):

        try:

            total_products = (
                self.product_repo.total_products()
            )

            total_sessions = (
                self.session_repo.total_sessions()
            )

            self.products_value.configure(
                text=str(total_products)
            )

            self.sessions_value.configure(
                text=str(total_sessions)
            )

        except Exception as error:

            self.products_value.configure(
                text="Error"
            )

            self.sessions_value.configure(
                text="Error"
            )

            print(
                f"Analytics error: {error}"
            )   