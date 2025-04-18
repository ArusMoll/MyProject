import unittest
from order_service import Order

class TestOrder(unittest.TestCase):
    def test_total_price(self):
        order = Order("Alice", [{"name": "Book", "price": 10.0, "quantity": 2}, {"name": "Pen", "price": 1.5}])
        self.assertAlmostEqual(order.total_price(), 21.5)

    def test_summary(self):
        order = Order("Bob", [{"name": "Laptop", "price": 999.99, "quantity": 1}])
        summary = order.summary()
        self.assertIn("Laptop", summary)
        self.assertIn("999.99", summary)

if __name__ == "__main__":
    unittest.main()
