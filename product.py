
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.active = True

    def update_price(self, new_price):
        self.price = new_price
        print(f"Product {self.name}'s price has been updated to {new_price}.")

    def suspend(self):
        self.active = False
        print(f"Product {self.name} has been suspended.")

