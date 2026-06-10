from collections import Counter

from app.database.repository import ProductRepository


class StatisticsEngine:

    def __init__(self):

        self.repository = ProductRepository()

    def total_products(self):

        return self.repository.total_products()

    def average_price(self):

        products = (
            self.repository.get_all_products()
        )

        prices = []

        for product in products:

            try:

                price_text = (
                    str(product.price)
                    .replace("$", "")
                    .replace("₹", "")
                    .replace(",", "")
                    .strip()
                )

                prices.append(
                    float(price_text)
                )

            except Exception:

                continue

        if not prices:

            return 0

        return round(
            sum(prices) / len(prices),
            2
        )

    def average_rating(self):

        products = (
            self.repository.get_all_products()
        )

        ratings = []

        for product in products:

            try:

                ratings.append(
                    float(product.rating)
                )

            except Exception:

                continue

        if not ratings:

            return 0

        return round(
            sum(ratings) / len(ratings),
            2
        )

    def availability_breakdown(self):

        products = (
            self.repository.get_all_products()
        )

        values = []

        for product in products:

            values.append(
                product.availability
            )

        return dict(
            Counter(values)
        )