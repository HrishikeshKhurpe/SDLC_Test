# Hrishikesh's Calculator

## Overview
Hrishikesh's Calculator is a Python-based calculator application that supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## File Structure
```
calculator/
├── calculator.py
└── tests/
    └── test_calculator.py
```

## Test Case Structure
The tests for the `Hrishikesh_Calculator` class are located in the `calculator/tests/test_calculator.py` file. The test suite covers the following operations:

- `test_add`
- `test_subtract`
- `test_multiply`
- `test_divide`

To run the tests, use the following command:

```
python -m unittest discover -s calculator/tests -p 'test_*.py'
```

## Run Book
To use the `Hrishikesh_Calculator`, follow these steps:

1. Import the `Hrishikesh_Calculator` class from the `calculator.calculator` module:

   ```python
   from calculator.calculator import Hrishikesh_Calculator
   ```

2. Create an instance of the `Hrishikesh_Calculator` class:

   ```python
   calculator = Hrishikesh_Calculator()
   ```

3. Use the provided methods to perform arithmetic operations:

   ```python
   result = calculator.add(2, 3)  # result = 5
   result = calculator.subtract(5, 3)  # result = 2
   result = calculator.multiply(2, 3)  # result = 6
   result = calculator.divide(6, 3)  # result = 2.0
   ```

## Dependencies
This project requires the following dependencies:

- Python 3.7 or higher

No additional libraries are required.

## Setup Instructions
1. Ensure you have Python 3.7 or higher installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory in your terminal.
4. You can now use the `Hrishikesh_Calculator` class in your Python scripts.

## Architecture
The `Hrishikesh_Calculator` class is the main component of this application. It provides methods for performing basic arithmetic operations. The class is designed to be easy to use and extensible, allowing for the addition of more advanced functionality in the future.

The test suite ensures the correctness of the arithmetic operations and provides a way to verify the behavior of the calculator.