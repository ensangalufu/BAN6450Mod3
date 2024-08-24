
class Policyholder:
    def __init__(self, policyholder_id, name):
        self.policyholder_id = policyholder_id
        self.name = name
        self.active = True
        self.products = []
        self.payments = []

    def register(self):
        self.active = True
        print(f"Policyholder {self.name} has been registered.")

    def suspend(self):
        self.active = False
        print(f"Policyholder {self.name} has been suspended.")

    def reactivate(self):
        self.active = True
        print(f"Policyholder {self.name} has been reactivated.")

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} has been added to policyholder {self.name}'s account.")

    def make_payment(self, payment):
        self.payments.append(payment)
        print(f"Payment of {payment.amount} has been made by {self.name}.")

    def display_details(self):
        print(f"Policyholder ID: {self.policyholder_id}")
        print(f"Name: {self.name}")
        print(f"Active: {'Yes' if self.active else 'No'}")
        print(f"Products: {[product.name for product in self.products]}")
        print(f"Payments: {[payment.amount for payment in self.payments]}")
