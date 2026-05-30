from os import wait
from typing import Any
from models.product import Product

    
class RetentionService:

    def get_cheapest(self, products, category: str, region: str) -> Product:
        same_category = [
            p for p in products
            if p.category.name == category
        ]

# при равной цене возвращается первый товар по порядку каталога
        return min(
            same_category,
            key=lambda p: p.price.get(region, float("inf"))
        )

    def build_offer(self, product, products, region: str) -> dict[str, Any]:
        cheapest = self.get_cheapest(products, product.category.name, region)

        current_price = product.price.get(region)

        if product.id == cheapest.id:
            return {
                "type": "discount",   
                "product": product,
                "old_price": current_price,
                "final_price": round(current_price * 0.95, 2)
            }

        return {
            "type": "alternative",
            "old_product": product,
            "product": cheapest,
            "old_price": current_price,
            "final_price": cheapest.price.get(region)
        }
