{
  "files": [
    {
      "file_path": "hrishikesh_calculator.py",
      "content": "\"\"\"
Hrishikesh's Calculator - A simple command-line calculator application.

Supports the following basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division
\"\"\"

from typing import Tuple

class HrishikeshCalculator:
    \"\"\"
    A simple calculator application that supports basic arithmetic operations.
    \"\"\"

    @staticmethod
    def add(a: float, b: float) -> float:
        \"\"\"
        Add two numbers.

        Args:
            a (float): The first number to add.
            b (float): The second number to add.

        Returns:
            float: The sum of the two numbers.
        \"\"\"
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        \"\"\"
        Subtract two numbers.

        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.

        Returns:
            float: The difference between the two numbers.
        \"\"\"
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        \"\"\"
        Multiply two numbers.

        Args:
            a (float): The first number to multiply.
            b (float): The second number to multiply.

        Returns:
            float: The product of the two numbers.
        \"\"\"
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        \"\"\"
        Divide two numbers.

        Args:
            a (float): The number to divide.
            b (float): The number to divide by.

        Returns:
            float: The quotient of the two numbers.

        Raises:
            ZeroDivisionError: If the divisor (b) is zero.
        \"\"\"
        if b == 0:
            raise ZeroDivisionError(\"Cannot divide by zero.\")
        return a / b

    @classmethod
    def calculate(cls, operation: str, a: float, b: float) -> float:
        \"\"\"
        Perform a basic arithmetic operation on two numbers.

        Args:
            operation (str): The arithmetic operation to perform. Can be one of: \"add\", \"subtract\", \"multiply\", \"divide\".
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the arithmetic operation.

        Raises:
            ValueError: If the operation is not one of the supported operations.
        \"\"\"
        operations = {
            \"add\": cls.add,
            \"subtract\": cls.subtract,
            \"multiply\": cls.multiply,
            \"divide\": cls.divide,
        }

        if operation not in operations:
            raise ValueError(f\"Invalid operation: {operation}. Supported operations are: {', '.join(operations.keys())}\")

        return operations[operation](a, b)

def main() -> None:
    \"\"\"
    The main entry point of the Hrishikesh's Calculator application.
    \"\"\"
    print(\"Welcome to Hrishikesh's Calculator!\")

    while True:
        try:
            a = float(input(\"Enter the first number: \"))
            b = float(input(\"Enter the second number: \"))
            operation = input(\"Enter the operation (+, -, *, /): \")

            result = HrishikeshCalculator.calculate(operation, a, b)
            print(f\"The result is: {result}\")

        except ValueError as e:
            print(f\"Error: {e}\")
        except ZeroDivisionError as e:
            print(f\"Error: {e}\")
        except KeyboardInterrupt:
            print(\"\\nExiting the calculator...\")
            break

if __name__ == \"__main__\":
    main()",
      "change_type": "create",
      "explanation": "This file implements the 'Hrishikesh's_Calculator' application, which supports basic arithmetic operations like addition, subtraction, multiplication, and division. The code follows clean code principles, including:

- Single Responsibility Principle: Each function/class has a clear, focused responsibility.
- DRY: Avoid duplication by using static methods for the arithmetic operations.
- Meaningful names: Variables, functions, and classes have clear, descriptive names.
- Error handling: Specific exception types are used, and errors are handled at the appropriate levels.
- Documentation: Docstrings are provided for all public functions and classes, and type hints are used throughout.
- Testability: The code is designed to be easily testable, with no hidden dependencies or global state.

The main function provides a simple command-line interface for the calculator, allowing users to perform arithmetic operations on two numbers.",
      "dependencies": []
    },
    {
      "file_path": "test_hrishikesh_calculator.py",
      "content": "\"\"\"
Unit and integration tests for the Hrishikesh's Calculator application.
\"\"\"

import unittest
from hrishikesh_calculator import HrishikeshCalculator

class TestHrishikeshCalculator(unittest.TestCase):
    \"\"\"
    Test suite for the Hrishikesh's Calculator application.
    \"\"\"

    def test_add(self):
        \"\"\"
        Test the addition operation.
        \"\"\"
        self.assertEqual(HrishikeshCalculator.add(2, 3), 5)
        self.assertEqual(HrishikeshCalculator.add(-1, 1), 0)
        self.assertEqual(HrishikeshCalculator.add(0, 0), 0)

    def test_subtract(self):
        \"\"\"
        Test the subtraction operation.
        \"\"\"
        self.assertEqual(HrishikeshCalculator.subtract(5, 3), 2)
        self.assertEqual(HrishikeshCalculator.subtract(1, 1), 0)
        self.assertEqual(HrishikeshCalculator.subtract(0, 0), 0)

    def test_multiply(self):
        \"\"\"
        Test the multiplication operation.
        \"\"\"
        self.assertEqual(HrishikeshCalculator.multiply(2, 3), 6)
        self.assertEqual(HrishikeshCalculator.multiply(-1, 1), -1)
        self.assertEqual(HrishikeshCalculator.multiply(0, 0), 0)

    def test_divide(self):
        \"\"\"
        Test the division operation.
        \"\"\"
        self.assertEqual(HrishikeshCalculator.divide(6, 3), 2)
        self.assertEqual(HrishikeshCalculator.divide(1, 1), 1)
        self.assertRaises(ZeroDivisionError, HrishikeshCalculator.divide, 1, 0)

    def test_calculate(self):
        \"\"\"
        Test the main calculate method.
        \"\"\"
        self.assertEqual(HrishikeshCalculator.calculate(\"add\", 2, 3), 5)
        self.assertEqual(HrishikeshCalculator.calculate(\"subtract\", 5, 3), 2)
        self.assertEqual(HrishikeshCalculator.calculate(\"multiply\", 2, 3), 6)
        self.assertEqual(HrishikeshCalculator.calculate(\"divide\", 6, 3), 2)
        self.assertRaises(ValueError, HrishikeshCalculator.calculate, \"invalid\", 1, 1)
        self.assertRaises(ZeroDivisionError, HrishikeshCalculator.calculate, \"divide\", 1, 0)

if __name__ == \"__main__\":
    unittest.main()",
      "change_type": "create",
      "explanation": "This file contains unit and integration tests for the Hrishikesh's Calculator application. The tests cover the following:

- Testing the individual arithmetic operations (add, subtract, multiply, divide)
- Testing the main `calculate` method, including handling of invalid operations and division by zero
- Using the `unittest` framework to structure an