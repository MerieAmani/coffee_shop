import pytest
from src.order import Order
from src.customer import Customer
from src.coffee import Coffee

def test_order_creation():
    customer = Customer("Grace")
    coffee = Coffee("Macchiato")
    order = Order(customer, coffee, 7.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 7.0

def test_order_price_validation():
    customer = Customer("Hank")
    coffee = Coffee("Ristretto")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)