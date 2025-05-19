class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a number between 1.0 and 10.0.")
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)