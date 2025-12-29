# Hrishikesh's Calculator

## Overview
Hrishikesh's Calculator is a Python-based calculator application that supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## File Structure
```
src/
└── features/
    └── calculator/
        ├── calculator.py
        └── tests/
            └── test_calculator.py
```

## Test Case Structure
The tests for the Hrishikesh's Calculator are located in the `src/features/calculator/tests/test_calculator.py` file. The test suite covers the basic arithmetic operations and includes tests for edge cases and error handling.

To run the tests, use the following command:

```bash
python -m unittest discover -s src/features/calculator/tests -p 'test_*.py'
```

## Run Book
To use the Hrishikesh's Calculator, follow these steps:

1. Import the `Hrishikesh_Calculator` class from the `src.features.calculator.calculator` module:

   ```python
   from src.features.calculator.calculator import Hrishikesh_Calculator
   ```

2. Create an instance of the `Hrishikesh_Calculator` class:

   ```python
   calculator = Hrishikesh_Calculator()
   ```

3. Use the arithmetic operation methods to perform calculations:

   ```python
   result = calculator.add(2, 3)  # Returns 5
   result = calculator.subtract(5, 3)  # Returns 2
   result = calculator.multiply(2, 3)  # Returns 6
   result = calculator.divide(6, 3)  # Returns 2.0
   ```

## Dependencies
The Hrishikesh's Calculator module does not have any external dependencies. It is a self-contained Python module.

## Setup Instructions
The Hrishikesh's Calculator module can be used as part of a larger Python project. No additional setup is required to use the calculator functionality.

## Architecture
The Hrishikesh's Calculator module consists of a single `Hrishikesh_Calculator` class that provides the basic arithmetic operations. The class is located in the `src/features/calculator/calculator.py` file.

The module also includes a test suite located in the `src/features/calculator/tests/test_calculator.py` file, which ensures the correct functionality of the arithmetic operations.