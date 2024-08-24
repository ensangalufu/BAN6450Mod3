
from policyholder import Policyholder
from product import Product
from payment import Payment

# Create some products
product1 = Product(1, "Health Insurance", 500)
product2 = Product(2, "Car Insurance", 300)

# Create some policyholders
policyholder1 = Policyholder(1, "John Doe")
policyholder2 = Policyholder(2, "Jane Smith")

# Register the policyholders
policyholder1.register()
policyholder2.register()

# Add products to policyholders
policyholder1.add_product(product1)
policyholder2.add_product(product2)

# Process payments
payment1 = Payment(1, 500, "2024-09-01")
payment2 = Payment(2, 300, "2024-09-05")

policyholder1.make_payment(payment1)
policyholder2.make_payment(payment2)

# Display details
print("\nPolicyholder 1 details:")
policyholder1.display_details()

print("\nPolicyholder 2 details:")
policyholder2.display_details()
