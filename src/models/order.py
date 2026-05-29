from dataclasses import dataclass
from models.product import Product

@dataclass
class Order:
    id: int
    region: str
    product: Product
    final_price: float
