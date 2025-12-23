""
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
The tests for the calculator functionality are located in the `src/features/calculator/tests/test_calculator.py` file. The `TestHrishikeshCalculator` class contains unit tests for the `add`, `subtract`, `multiply`, and `divide` methods of the `Hrishikesh_Calculator` class.

To run the tests, use the following command:

```
python -m unittest discover -s src/features/calculator/tests -p "test_*.py"
```

## Run Book
To use the Hrishikesh's Calculator, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone the repository and navigate to the project directory.
3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the calculator example:
   ```python
   from src.features.calculator.calculator import Hrishikesh_Calculator

   calculator = Hrishikesh_Calculator()
   print(calculator.add(5, 3))  # Output: 8.0
   print(calculator.subtract(10, 4))  # Output: 6.0
   print(calculator.multiply(2, 6))  # Output: 12.0
   print(calculator.divide(15, 3))  # Output: 5.0
   ```

## Dependencies
The Hrishikesh's Calculator application has no external dependencies. It uses only the Python standard library.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.

## Architecture
The Hrishikesh's Calculator application is designed with a single class, `Hrishikesh_Calculator`, that encapsulates the basic arithmetic operations. The class uses logging to provide information about the operations being performed.

The application follows the SOLID principles of object-oriented design, with each method in the `Hrishikesh_Calculator` class having a single responsibility. The code is organized into appropriate folders and files to maintain modularity and maintainability.
""