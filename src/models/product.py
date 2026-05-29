from dataclasses import dataclass
from models.categories import Category

@dataclass
class Product:
    id: int
    name: str
    category: Category
    price: dict[str, float]
