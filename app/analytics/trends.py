from collections import defaultdict

from app.database.repository import (
    ProductRepository
)


class TrendAnalyzer:

    def __init__(self):

        self.repository = (
            ProductRepository()
        )

    def products_by_date(self):

        products = (
            self.repository
            .get_all_products()
        )

        results = defaultdict(int)

        for product in products:

            date_key = (
                product.scraped_at
                .strftime("%Y-%m-%d")
            )

            results[date_key] += 1

        return dict(results)

    def top_sources(
        self,
        limit=10
    ):

        products = (
            self.repository
            .get_all_products()
        )

        results = defaultdict(int)

        for product in products:

            results[
                product.source_url
            ] += 1

        sorted_results = sorted(
            results.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return sorted_results[:limit]

    def top_rated_products(
        self,
        limit=10
    ):

        products = (
            self.repository
            .get_all_products()
        )

        valid_products = []

        for product in products:

            try:

                rating = float(
                    product.rating
                )

                valid_products.append(
                    (
                        product.name,
                        rating
                    )
                )

            except Exception:

                continue

        valid_products.sort(
            key=lambda item: item[1],
            reverse=True
        )

        return valid_products[:limit]