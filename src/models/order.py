from dataclasses import dataclass
from models.product import Product


@dataclass
class Order:
    product_id: int
    product_name: Product
    region: str
    final_price: float
