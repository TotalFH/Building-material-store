import sys

from models.product import Product
from views.console_view import ConsoleView
from services.catalog_service import CatalogService
from services.order_service import OrderService
from services.retention_service import RetentionService


class App:
    def __init__(self):
        self.view = ConsoleView()
        self.catalog = CatalogService()
        self.order = OrderService()
        self.retention = RetentionService()
        self._products: list[Product] | None = None

    def run(self) -> None:
        self._products = self._load_catalog()

        while True:
            regions = self.catalog.get_regions(self._products)
            region = self.view.choose_region(regions)
            if region is None:
                break
            self._handle_region(region)

    def _handle_region(self, region: str) -> None:
        while True:
            self.view.show_products(self._products, region)
            product = self.view.choose_product(self._products)
            if product is None:
                break
            self._handle_product(product, region)

    def _handle_product(self, product: Product, region: str) -> None:
        decision = self.view.confirm_order()

        if decision == "back":
            return
        if decision == "yes":
            self._handle_confirm(product, region)
            return
        if decision == "no":
            self._handle_retention(product, region)

    def _handle_confirm(self, product, region: str) -> None:
        order = self.order.create_order(product, region)
        try:
            self.order.save_order(order)
            self.view.show_success()
        except RuntimeError as e:
            self.view.show_error(str(e))
            sys.exit(1)

    def _handle_retention(self, product, region: str) -> None:
        offer = self.retention.build_offer(product, self._products, region)
        self.view.show_offer(offer)

        if self.view.confirm_order() == "yes":
            order = self.order.create_order(offer["product"], region, override_price=offer["final_price"])
            self.order.save_order(order)
            self.view.show_success()

    def _load_catalog(self) -> list[Product]:
        try:
            return self.catalog.get_products()
        except RuntimeError as e:
            self.view.show_error(str(e))
            sys.exit(1)
