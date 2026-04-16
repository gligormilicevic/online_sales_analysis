from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager = ProductManager()
# p1 = Product("Laptop", 1200, 5)
p1 = Product("Super Laptop", 1200, 5)
p2 = Product("Mouse", 25, 20)

manager.add_product(p1)
manager.add_product(p2)

print("Inventory List:")
manager.display_all_products()
print(f"Total Value: {manager.total_inventory_value()}")


# from cart import Cart
# import random

my_cart = Cart()
# Add 3 random items (for this example, we'll just add the existing ones)
available = manager.products
for _ in range(3):
    if available:
        my_cart.add_to_cart(random.choice(available))

my_cart.display_cart()
print(f"Cart Total: {my_cart.calculate_total()}")
>>>>>> > add-cart-functionality
