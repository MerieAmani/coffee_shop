import pytest
from src.coffee import Coffee
from src.customer import Customer
from src.order import Order

def test_coffee_creation():
    coffee = Coffee("Americano")
    assert coffee.name == "Americano"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("A")

def test_coffee_orders():
    coffee = Coffee("Mocha")
    customer = Customer("Dave")
    order = customer.create_order(coffee, 6.0)
    assert order in coffee.orders()

def test_coffee_customers():
    coffee = Coffee("Flat White")
    customer1 = Customer("Eve")
    customer2 = Customer("Frank")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    assert customer1 in coffee.customers()
    assert customer2 in coffee.customers()