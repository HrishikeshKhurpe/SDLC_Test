""
# Hrishikesh's Calculator

## Overview
Hrishikesh's Calculator is a Python-based calculator application that supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## File Structure
```
calculator/
├── calculator.py
└── tests/
    ├── test_calculator.py
    └── test_calculator_integration.py
```

## Test Case Structure
The tests for the Hrishikesh's Calculator are organized into two files:

1. `test_calculator.py`: Contains unit tests for the individual calculator operations.
2. `test_calculator_integration.py`: Contains integration tests to verify the overall functionality of the calculator.

To run the tests, use the following command:

```
python -m unittest discover -s calculator/tests -p "test_*.py"
```

## Run Book
To use the Hrishikesh's Calculator, follow these steps:

1. Import the `Hrishikesh_Calculator` class from the `calculator.py` file.
2. Create an instance of the `Hrishikesh_Calculator` class.
3. Call the appropriate methods (add, subtract, multiply, divide) with the desired arguments.

Example usage:

```python
from calculator.calculator import Hrishikesh_Calculator

calculator = Hrishikesh_Calculator()
result = calculator.add(2, 3)
print(result)  # Output: 5
```

## Dependencies
The Hrishikesh's Calculator does not have any external dependencies. It is a self-contained Python module.

## Setup Instructions
1. Ensure you have Python 3.x installed on your system.
2. Clone the repository containing the Hrishikesh's Calculator code.
3. Navigate to the project directory in your terminal.
4. You can now use the calculator by importing the `Hrishikesh_Calculator` class from the `calculator.py` file.

## API Documentation
The Hrishikesh's Calculator provides the following methods:

- `add(a: float, b: float) -> float`: Adds two numbers and returns the result.
- `subtract(a: float, b: float) -> float`: Subtracts two numbers and returns the result.
- `multiply(a: float, b: float) -> float`: Multiplies two numbers and returns the result.
- `divide(a: float, b: float) -> float`: Divides two numbers and returns the result. Raises a `ZeroDivisionError` if the second argument is zero.

## Architecture
The Hrishikesh's Calculator is a simple, standalone Python module that provides basic arithmetic operations. It follows a straightforward object-oriented design, with the `Hrishikesh_Calculator` class encapsulating the calculator functionality.

The module also includes unit tests and integration tests to ensure the correctness of the calculator operations.
""