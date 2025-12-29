# Hrishikesh's Calculator

## Overview
Hrishikesh's Calculator is a Python-based calculator application that supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## File Structure
```
hrishikeshs_calculator/
├── calculator.py
└── tests/
    └── test_calculator.py
```

## Test Case Structure
The test cases for the calculator are located in the `hrishikeshs_calculator/tests/test_calculator.py` file. The `TestHrishikeshCalculator` class contains unit tests for each of the calculator operations (add, subtract, multiply, divide).

To run the tests, use the following command:

```bash
python -m unittest discover -s hrishikeshs_calculator/tests -p "test_*.py"
```

## Run Book
To use the Hrishikesh's Calculator, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone the repository and navigate to the project directory.
3. Run the calculator script:

```bash
python hrishikeshs_calculator/calculator.py
```

This will execute the example usage of the calculator, demonstrating the various operations.

## Dependencies
The Hrishikesh's Calculator application does not have any external dependencies. It uses only the standard Python library.

## Setup Instructions
1. Clone the repository:

```bash
git clone https://github.com/HrishikeshKhurpe/SDLC_Test.git
```

2. Navigate to the project directory:

```bash
cd SDLC_Test
```

3. Run the calculator script:

```bash
python hrishikeshs_calculator/calculator.py
```

## Architecture
The Hrishikesh's Calculator application consists of a single module, `calculator.py`, which contains the `Hrishikesh_Calculator` class. This class provides the implementation for the basic arithmetic operations (add, subtract, multiply, divide).

The `test_calculator.py` file contains the unit tests for the calculator operations, ensuring the correctness of the implementation.