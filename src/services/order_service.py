import json

from models.order import Order
from dataclasses import asdict


class OrderService:
    def create_order(self, product, region: str, override_price: float | None = None) -> Order:
        return Order(
            product_id=product.id,
            product_name=product.name,
            region=region,
            final_price=override_price if override_price is not None else product.price[region],
        )

    def save_order(self, order) -> None:
        try:
            order_data = asdict(order)

            file_name = f"orders/order_{order.product_id}.json"

            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(
                    order_data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )
        except OSError as e:
            raise RuntimeError(f"Ошибка сохранения заказа: {e}") from e
