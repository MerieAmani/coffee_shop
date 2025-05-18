# Coffee Shop Domain Model

This project models a Coffee Shop domain using object-oriented programming principles in Python. It includes three main entities: `Customer`, `Coffee`, and `Order`, which interact with each other to simulate a coffee shop's operations.

## Project Structure

```
coffee_shop
├── src
│   ├── customer.py       # Defines the Customer class with order management.
│   ├── coffee.py         # Defines the Coffee class with order tracking.
│   ├── order.py          # Defines the Order class linking customers and coffees.
│   └── debug.py          # For interactive testing and debugging of the classes.
├── tests
│   ├── test_customer.py   # Test cases for the Customer class.
│   ├── test_coffee.py     # Test cases for the Coffee class.
│   └── test_order.py      # Test cases for the Order class.
├── Pipfile                # Configuration file for pipenv dependencies.
├── Pipfile.lock           # Locks the versions of dependencies.
└── README.md              # Documentation for the project.
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd coffee_shop
   ```

2. **Set up the virtual environment**:
   ```
   pipenv install
   pipenv shell
   ```

3. **Run tests** (optional):
   ```
   pytest
   ```

## Usage

- Create instances of `Customer` and `Coffee`.
- Use the `create_order(coffee, price)` method in the `Customer` class to place orders.
- Retrieve orders and unique coffees for each customer using the `orders()` and `coffees()` methods.
- Analyze coffee orders using methods in the `Coffee` class like `num_orders()` and `average_price()`.
- Use the `most_aficionado(coffee)` class method in the `Customer` class to find the customer who has spent the most on a specific coffee.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.