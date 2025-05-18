import pytest
from coffee_shop.src.coffee import Coffee
from coffee_shop.src.customer import Customer
from coffee_shop.src.order import Order

def test_coffee_initialization():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("A") 
    with pytest.raises(ValueError):
        Coffee("Cappuccino" * 10)  
def test_coffee_orders():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    order = Order(customer, coffee, 5.0)
    assert coffee.orders() == [order]

def test_coffee_customers():
    coffee = Coffee("Mocha")
    customer1 = Customer("Bob")
    customer2 = Customer("Charlie")
    order1 = Order(customer1, coffee, 4.0)
    order2 = Order(customer2, coffee, 6.0)
    assert set(coffee.customers()) == {customer1, customer2}

def test_coffee_num_orders():
    coffee = Coffee("Americano")
    customer = Customer("David")
    Order(customer, coffee, 3.0)
    Order(customer, coffee, 4.0)
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Flat White")
    customer = Customer("Eve")
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 7.0)
    assert coffee.average_price() == 6.0