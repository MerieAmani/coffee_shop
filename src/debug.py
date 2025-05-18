from customer import Customer
from coffee import Coffee

# Create customer
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Create coffee
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create order
customer1.create_order(coffee1, 5.0)
customer1.create_order(coffee2, 6.0)
customer2.create_order(coffee1, 4.5)

# Debugging 
print(f"Customer {customer1.name} has ordered: {[coffee.name for coffee in customer1.coffees()]}")
print(f"Coffee {coffee1.name} has been ordered {coffee1.num_orders()} times.")
print(f"Average price of {coffee1.name}: {coffee1.average_price()}")