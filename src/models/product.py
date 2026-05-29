from dataclasses import dataclass
from .category import Category

@dataclass
class Product:
    id: int
    name: str
    category: Category
    price: dict[str, float]
