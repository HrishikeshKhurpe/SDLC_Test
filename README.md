# Hrishikesh's Calculator

## Overview
The `Hrishikesh's_Calculator` is a Python-based calculator application that supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## File Structure
```
hrishikeshs_calculator/
├── calculator.py
└── tests/
    └── test_calculator.py
```

## Test Case Structure
The test cases for the calculator are located in the `hrishikeshs_calculator/tests/test_calculator.py` file. The test suite covers the following operations:
- Addition
- Subtraction
- Multiplication
- Division

To run the tests, use the following command:
```
python -m unittest discover -s hrishikeshs_calculator/tests -p 'test_*.py'
```

## Run Book
To use the `Hrishikesh's_Calculator`, follow these steps:

1. Import the `Hrishikesh_Calculator` class from the `hrishikeshs_calculator.calculator` module:
   ```python
   from hrishikeshs_calculator.calculator import Hrishikesh_Calculator
   ```
2. Create an instance of the `Hrishikesh_Calculator` class:
   ```python
   calculator = Hrishikesh_Calculator()
   ```
3. Use the calculator methods to perform arithmetic operations:
   ```python
   result = calculator.add(2, 3)
   print(result)  # Output: 5

   result = calculator.subtract(5, 3)
   print(result)  # Output: 2

   result = calculator.multiply(2, 3)
   print(result)  # Output: 6

   result = calculator.divide(6, 3)
   print(result)  # Output: 2.0
   ```

## Dependencies
The `Hrishikesh's_Calculator` module does not have any external dependencies. It is a self-contained Python module.

## Setup Instructions
1. Ensure you have Python 3.x installed on your system.
2. Clone the repository containing the `Hrishikesh's_Calculator` module.
3. Navigate to the project directory in your terminal.
4. You can now use the `Hrishikesh_Calculator` class in your Python scripts.

## API Documentation
The `Hrishikesh_Calculator` class provides the following methods:

- `add(a, b)`: Adds two numbers and returns the result.
- `subtract(a, b)`: Subtracts two numbers and returns the result.
- `multiply(a, b)`: Multiplies two numbers and returns the result.
- `divide(a, b)`: Divides two numbers and returns the result. Raises a `ZeroDivisionError` if the divisor is zero.

## Architecture
The `Hrishikesh's_Calculator` module consists of a single class, `Hrishikesh_Calculator`, which encapsulates the basic arithmetic operations. The module follows a simple and straightforward design, with each operation implemented as a separate method within the class.

The test suite, located in the `hrishikeshs_calculator/tests/test_calculator.py` file, ensures the correctness of the calculator's functionality by covering various test cases for each operation.
