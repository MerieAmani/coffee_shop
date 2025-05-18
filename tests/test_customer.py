import pytest
from coffee_shop.src.customer import Customer
from coffee_shop.src.coffee import Coffee

def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("") 
    with pytest.raises(ValueError):
        Customer("A very long name exceeding 15 characters") 

def test_create_order():
    customer = Customer("Bob")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_orders_method():
    customer = Customer("Charlie")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Cappuccino")
    customer.create_order(coffee1, 4.0)
    customer.create_order(coffee2, 6.0)
    orders = customer.orders()
    assert len(orders) == 2

def test_coffees_method():
    customer = Customer("Diana")
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Americano")
    customer.create_order(coffee1, 3.5)
    customer.create_order(coffee2, 4.5)
    unique_coffees = customer.coffees()
    assert len(unique_coffees) == 2
    assert coffee1 in unique_coffees
    assert coffee2 in unique_coffees