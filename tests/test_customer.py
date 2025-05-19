import pytest
from src.customer import Customer
from src.coffee import Coffee
from src.order import Order

def test_customer_creation():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_orders():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order in customer.orders()

def test_customer_coffees():
    customer = Customer("Charlie")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Cappuccino")
    customer.create_order(coffee1, 4.0)
    customer.create_order(coffee2, 5.0)
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()