class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def calculate_total(self):
        return sum(item.price for item in self.cart_items)

    def display_cart(self):
        print("Items in Cart:")
        for item in self.cart_items:
            print(f"- {item.name}: ${item.price}")
