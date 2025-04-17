from datetime import datetime

class Order:
    def __init__(self, customer_name: str, items: list[dict]):
        self.customer_name = customer_name
        self.items = items
        self.timestamp = datetime.now()
    
    def total_price(self) -> float:
        return sum(item["price"] * item.get("quantity", 1) for item in self.items)

    def summary(self) -> str:
        item_list = ", ".join([f"{i['name']} x{i.get('quantity',1)}" for i in self.items])
        return f"Order for {self.customer_name}: {item_list}. Total: ${self.total_price():.2f}"
