from product import Product
from product_manager import ProductManager

manager = ProductManager()
# p1 = Product("Laptop", 1200, 5)
p1 = Product("Super Laptop", 1200, 5)
p2 = Product("Mouse", 25, 20)

manager.add_product(p1)
manager.add_product(p2)

print("Inventory List:")
manager.display_all_products()
print(f"Total Value: {manager.total_inventory_value()}")


# Edit main.py manually to change product names/quantities and delete display lines.
