class Customer:
    all_customers = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self.name = name
        Customer.all_customers.append(self)

    def orders(self):
        from .order import Order
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from .order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from .order import Order
        spending = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price
        return max(spending, key=lambda customer: spending.get(customer, 0), default=None)