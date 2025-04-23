from datetime import datetime

from api.models.pydantic.product import Product
from api.subscriptions.product_status import ProductStatus


class ProductLogic:

    def __init__(self, product: Product) -> None:
        self._product_name = product.name
        self._url = product.url
        self._last_fetch_time: datetime | None = None
        self._status = ProductStatus.PENDING

    def update_url(self, url: str) -> None:
        """Updates the URL for the product"""
        # todo: type checking, valid url checking
        self._url = url

    def get_status(self) -> ProductStatus:
        return self._status

    def check_status(self) -> bool:
        """Scrapes the product URL to check if the product is in stock"""
        # if item in stock:
        #   self._status = ProductStatus.IN_STOCK
        return False

    def __repr__(self):
        return (
            f"Product {self._product_name!r}: status={self._status} (url={self._url})"
        )
