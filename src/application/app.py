from views.console_view import ConsoleView
from services.catalog_service import CatalogService 

class App:

    def __init__(self):
        self.view = ConsoleView()
        self.catalog = CatalogService()
        self.order = OrderService()
        self.retention = RetentionService()

    def run(self):
        region = self.view.choose_region()

        products = self.catalog.get_products()

        self.view.show_products(products, region)

        product = self.view.choose_product(products)

        if self.view.confirm_order():
            order = self.order.create_order(product, region)
            self.order.save(order)
        else:
            offer = self.retention.get_offer(product, products, region)
            self.view.show_offer(offer)
