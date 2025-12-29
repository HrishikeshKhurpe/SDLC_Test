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
The test cases for the calculator are located in the `src/features/calculator/tests/test_calculator.py` file. The test suite covers all the basic arithmetic operations, including edge cases and error handling.

To run the tests, use the following command:

```
python -m unittest discover -s src/features/calculator/tests -p 'test_*.py'
```

## Run Book
To use the Hrishikesh's Calculator, follow these steps:

1. Ensure you have Python 3.x installed on your system.
2. Clone the repository and navigate to the project directory.
3. (Optional) Create a virtual environment and activate it.
4. Install the required dependencies (if any) using `pip install -r requirements.txt`.
5. Import the `Hrishikesh_Calculator` class from `src.features.calculator.calculator` and create an instance of the class.
6. Use the provided methods (`add`, `subtract`, `multiply`, `divide`) to perform the desired arithmetic operations.

Example usage:

```python
from src.features.calculator.calculator import Hrishikesh_Calculator

calc = Hrishikesh_Calculator()
result = calc.add(2, 3)
print(result)  # Output: 5
```

## Dependencies
This project does not have any external dependencies. It uses only standard Python libraries.

## Setup Instructions
1. Clone the repository: `git clone https://github.com/HrishikeshKhurpe/SDLC_Test.git`
2. Navigate to the project directory: `cd SDLC_Test`
3. (Optional) Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix/Linux: `source venv/bin/activate`
5. Install the required dependencies (if any): `pip install -r requirements.txt`
6. You're now ready to use the Hrishikesh's Calculator!

## API Documentation
The Hrishikesh's Calculator provides the following methods:

- `add(a, b)`: Adds two numbers and returns the result.
- `subtract(a, b)`: Subtracts one number from another and returns the result.
- `multiply(a, b)`: Multiplies two numbers and returns the result.
- `divide(a, b)`: Divides one number by another and returns the result. Raises a `ValueError` if the divisor is zero.

All methods raise a `ValueError` if the input values are not numeric.

## Architecture
The Hrishikesh's Calculator is a standalone Python module that provides basic arithmetic functionality. It follows a simple class-based design, with each arithmetic operation implemented as a method on the `Hrishikesh_Calculator` class. The module also includes comprehensive error handling and logging to ensure a robust and user-friendly experience.