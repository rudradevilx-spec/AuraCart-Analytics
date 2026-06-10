import matplotlib.pyplot as plt

from app.analytics.statistics import (
    StatisticsEngine
)

from app.analytics.trends import (
    TrendAnalyzer
)


class ChartGenerator:

    def __init__(self):

        self.statistics = (
            StatisticsEngine()
        )

        self.trends = (
            TrendAnalyzer()
        )

    def availability_chart(self):

        data = (
            self.statistics
            .availability_breakdown()
        )

        if not data:

            return

        plt.figure(
            figsize=(8, 5)
        )

        plt.pie(
            list(data.values()),
            labels=list(data.keys()),
            autopct="%1.1f%%"
        )

        plt.title(
            "Availability Distribution"
        )

        plt.show()

    def product_growth_chart(self):

        data = (
            self.trends
            .products_by_date()
        )

        if not data:

            return

        plt.figure(
            figsize=(10, 5)
        )

        plt.plot(
            list(data.keys()),
            list(data.values())
        )

        plt.title(
            "Products Collected Over Time"
        )

        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        plt.show()