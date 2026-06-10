from bs4 import BeautifulSoup


class GenericProfile:

    PRODUCT_SELECTORS = [
        ".product",
        ".product-card",
        ".product-item",
        ".item",
        "[data-product]"
    ]

    NAME_SELECTORS = [
        ".product-title",
        ".title",
        "h2",
        "h3",
        "h4"
    ]

    PRICE_SELECTORS = [
        ".price",
        ".product-price",
        "[data-price]"
    ]

    RATING_SELECTORS = [
        ".rating",
        ".stars",
        "[data-rating]"
    ]

    AVAILABILITY_SELECTORS = [
        ".availability",
        ".stock",
        ".in-stock"
    ]

    @staticmethod
    def detect_products(soup):

        for selector in GenericProfile.PRODUCT_SELECTORS:

            products = soup.select(selector)

            if products:

                return products

        return []