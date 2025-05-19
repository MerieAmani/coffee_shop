from src.customer import Customer
from src.coffee import Coffee
from src.order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = alice.create_order(latte, 5.0)
order2 = bob.create_order(espresso, 4.0)

# Debug relationships
print("Alice's orders:", alice.orders())
print("Latte's customers:", latte.customers())
print("Espresso's number of orders:", espresso.num_orders())
print("Latte's average price:", latte.average_price())