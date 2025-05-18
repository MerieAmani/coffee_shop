import pytest
from coffee_shop.src.customer import Customer
from coffee_shop.src.coffee import Coffee
from coffee_shop.src.order import Order

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_price_validation():
    customer = Customer("Bob")
    coffee = Coffee("Latte")

    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  

    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0) 

def test_order_relationships():
    customer = Customer("Charlie")
    coffee1 = Coffee("Cappuccino")
    coffee2 = Coffee("Mocha")
    
    order1 = Order(customer, coffee1, 4.0)
    order2 = Order(customer, coffee2, 6.0)

    assert order1.customer == customer
    assert order1.coffee == coffee1
    assert order2.customer == customer
    assert order2.coffee == coffee2

def test_order_customer_property():
    customer = Customer("Diana")
    coffee = Coffee("Americano")
    order = Order(customer, coffee, 3.5)

    assert order.customer == customer

def test_order_coffee_property():
    customer = Customer("Ethan")
    coffee = Coffee("Flat White")
    order = Order(customer, coffee, 4.5)

    assert order.coffee == coffee