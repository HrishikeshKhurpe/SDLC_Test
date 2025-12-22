{
  "files": [
    {
      "file_path": "hrishikesh_calculator/calculator.py",
      "content": "\"\"\"
This module implements the core functionality of the Hrishikesh's Calculator application.
It provides basic arithmetic operations like addition, subtraction, multiplication, and division.
\"\"\"

from typing import Union

class Calculator:
    \"\"\"
    Hrishikesh's Calculator class.
    \"\"\"

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        \"\"\"
        Add two numbers.

        Args:
            a (Union[int, float]): The first number to add.
            b (Union[int, float]): The second number to add.

        Returns:
            Union[int, float]: The sum of the two numbers.

        Raises:
            TypeError: If either `a` or `b` is not a number.
        \"\"\"
        try:
            return a + b
        except TypeError as e:
            raise TypeError(f"Invalid input types: {a} and {b}") from e

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        \"\"\"
        Subtract two numbers.

        Args:
            a (Union[int, float]): The number to subtract from.
            b (Union[int, float]): The number to subtract.

        Returns:
            Union[int, float]: The difference between the two numbers.

        Raises:
            TypeError: If either `a` or `b` is not a number.
        \"\"\"
        try:
            return a - b
        except TypeError as e:
            raise TypeError(f"Invalid input types: {a} and {b}") from e

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        \"\"\"
        Multiply two numbers.

        Args:
            a (Union[int, float]): The first number to multiply.
            b (Union[int, float]): The second number to multiply.

        Returns:
            Union[int, float]: The product of the two numbers.

        Raises:
            TypeError: If either `a` or `b` is not a number.
        \"\"\"
        try:
            return a * b
        except TypeError as e:
            raise TypeError(f"Invalid input types: {a} and {b}") from e

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        \"\"\"
        Divide two numbers.

        Args:
            a (Union[int, float]): The number to divide.
            b (Union[int, float]): The number to divide by.

        Returns:
            Union[int, float]: The quotient of the division.

        Raises:
            TypeError: If either `a` or `b` is not a number.
            ZeroDivisionError: If `b` is zero.
        \"\"\"
        try:
            return a / b
        except TypeError as e:
            raise TypeError(f"Invalid input types: {a} and {b}") from e
        except ZeroDivisionError as e:
            raise ZeroDivisionError("Cannot divide by zero") from e
",
      "change_type": "create",
      "explanation": "Implement the main calculator module with the basic arithmetic operations.",
      "dependencies": [],
      "callers_affected": [],
      "backward_compatible": true,
      "test_updates_required": ["tests/unit/test_calculator.py"],
      "documentation_updates": ["README.md"]
    },
    {
      "file_path": "tests/unit/test_calculator.py",
      "content": "\"\"\"
Unit tests for the Hrishikesh's Calculator module.
\"\"\"

import unittest
from hrishikesh_calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    \"\"\"
    Test case for the Calculator class.
    \"\"\"

    def test_add(self):
        \"\"\"
        Test the add method.
        \"\"\"
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-2, 3), 1)
        self.assertEqual(Calculator.add(2.5, 3.7), 6.2)
        self.assertRaises(TypeError, Calculator.add, "2", 3)

    def test_subtract(self):
        \"\"\"
        Test the subtract method.
        \"\"\"
        self.assertEqual(Calculator.subtract(5, 3), 2)
        self.assertEqual(Calculator.subtract(3, 5), -2)
        self.assertEqual(Calculator.subtract(10.5, 4.2), 6.3)
        self.assertRaises(TypeError, Calculator.subtract, "5", 3)

    def test_multiply(self):
        \"\"\"
        Test the multiply method.
        \"\"\"
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertEqual(Calculator.multiply(-2, 3), -6)
        self.assertEqual(Calculator.multiply(2.5, 3.7), 9.25)
        self.assertRaises(TypeError, Calculator.multiply, "2", 3)

    def test_divide(self):
        \"\"\"
        Test the divide method.
        \"\"\"
        self.assertEqual(Calculator.divide(6, 3), 2)
        self.assertEqual(Calculator.divide(10, 4), 2.5)
        self.assertRaises(ZeroDivisionError, Calculator.divide, 10, 0)
        self.assertRaises(TypeError, Calculator.divide, "6", 3)

if __name__ == '__main__':
    unittest.main()
",
      "change_type": "create",
      "explanation": "Implement unit tests for the calculator module.",
      "dependencies": ["hrishikesh_calculator/calculator.py"],
      "callers_affected": [],
      "backward_compatible": true,
      "test_updates_required": [],
      "documentation_updates": []
    },
    {
      "file_path": "tests/integration/test_calculator_integration.py",
      "content": "\"\"\"
Integration tests for the Hrishikesh's Calculator application.
\"\"\"

import unittest
from hrishikesh_calculator.calculator import Calculator
from hrishikesh_calculator.app import CalculatorApp

class TestCalculatorIntegration(unittest.TestCase):
    \"\"\"
    Integration test case for the Calculator application.
    \"\"\"

    def test_calculator_integration(self):
        \"\"\"
        Test the integration of the Calculator class and the CalculatorApp.
        \"\"\"
        app = CalculatorApp()

        # Test addition
        self.assertEqual(app.calculate(2, 3, "+"), 5)
        self.assertEqual(app.calculate(-2, 3, "+"), 1)
        self.assertEqual(app.calculate(2.5, 3.7, "+"), 6.2)

        # Test subtraction
        self.assertEqual(app.calculate(5, 3, "-"), 2)
        self.assertEqual(app.calculate(3, 5, "-"), -2)
        self.assertEqual(app.calculate(10.5, 4.2, "-"), 6.3)

        # Test multiplication
        self.assertEqual(app.calculate(2, 3, "*"), 6)
        self.assertEqual(app.calculate(-2, 3, "*"), -6)
        self.assertEqual(app.calculate(2.5, 3.7, "*"), 9.25)

        # Test division
        self.assertEqual(app.calculate(6, 3, "/"), 2)
        self.assertEqual(app.calculate(10, 4, "/"), 2.5)
        self.assertRaises(ZeroDivisionError, app.calculate, 10, 0, "/")

if __name__ == '__main__':
    unittest.main()
",
      "change_