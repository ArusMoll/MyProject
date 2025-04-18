from datetime import datetime
import uuid

class Order:
    def __init__(self, customer_name: str, items: list[dict]):
        self.order_id = str(uuid.uuid4())  # Унікальний ідентифікатор замовлення
        self.customer_name = customer_name
        self.items = items
        self.timestamp = datetime.now()
    
    def total_price(self) -> float:
        return sum(item["price"] * item.get("quantity", 1) for item in self.items)

    def add_item(self, item: dict) -> None:
        """Додає новий товар до замовлення"""
        self.items.append(item)

    def summary(self) -> str:
        item_list = ", ".join([f"{i['name']} x{i.get('quantity', 1)}" for i in self.items])
        return (f"Order ID: {self.order_id}\n"
                f"Customer: {self.customer_name}\n"
                f"Items: {item_list}\n"
                f"Total: ${self.total_price():.2f}\n"
                f"Created: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    def __str__(self):
        return self.summary()
