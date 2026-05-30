import json
from typing import Any

from models.categories import Category
from models.product import Product


class CatalogService:
    PATH = "data/materials.json"
    
    def get_regions(self, products: list[Product]) -> list[str]:
        regions = set()
        for product in products:
            regions.update(product.price.keys())
        return sorted(regions)

    def load_products_from_json(self) -> list[dict[str, Any]]:
        try:
            with open(self.PATH, encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            raise RuntimeError(f"Файл каталога не найден: {self.PATH}") from None

        except json.JSONDecodeError as e:
            raise RuntimeError(f"Каталог повреждён: строка {e.lineno}, {e.msg}") from e

    def get_products(self) -> list[Product]:
        data = self.load_products_from_json()  

        products = []
        for item in data:
            try:
                product = Product(
                    id=item["id"],
                    name=item["name"],
                    category=Category(**item["category"]),
                    price=item["prices"],
                )
            except KeyError as e:
                raise RuntimeError(f"Отсутствует поле {e} в товаре: {item}") from e
            products.append(product)

        return products
