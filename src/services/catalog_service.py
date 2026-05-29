import json
import typing

from models.categories import Category
from models.product import Product

class CatalogService:

    def load_products_from_json(self) -> list[dict[str, Any]]:
        with open("data/materials.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    
    def get_products(self) -> list[Product]:
        data = self.load_products_from_json()

        products = []

        for item in data:
            product = Product(
                id = item["id"],
                name = item["name"],
                category = Category(**item["category"]),
                prices = item["prices"]
                    )
            products.append(product)
            
        return products


