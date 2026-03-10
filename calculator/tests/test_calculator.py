import unittest
from calculator.calculator import Calculator
from calculator.ui_controller import CalculatorUIController
import logging

# Suppress logging during tests to keep test output clean
logging.disable(logging.CRITICAL)

class TestCalculator(unittest.TestCase):
    """
    Tests for the core Calculator arithmetic logic.
    """
    def setUp(self):
        """Set up a new Calculator instance before each test."""
        self.calculator = Calculator()

    def test_add(self):
        """Test the addition operation."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)
        self.assertEqual(self.calculator.add(0.5, 0.5), 1.0)

    def test_subtract(self):n        """Test the subtraction operation."""
        self.assertEqual(self.calculator.subtract(5, 2), 3)
        self.assertEqual(self.calculator.subtract(2, 5), -3)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(1.5, 0.5), 1.0)

    def test_multiply(self):
        """Test the multiplication operation."""
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(2.5, 2), 5.0)

    def test_divide(self):
        """Test the division operation."""
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        self.assertEqual(self.calculator.divide(-6, 3), -2)
        self.assertEqual(self.calculator.divide(0, 5), 0)

    def test_divide_by_zero(self):
        """Test division by zero raises a ValueError."""
        with self.assertRaises(ValueError) as cm:
            self.calculator.divide(10, 0)
        self.assertEqual(str(cm.exception), "Cannot divide by zero")

class TestCalculatorUIController(unittest.TestCase):
    """
    Tests for the CalculatorUIController, focusing on expression evaluation.
    """
    def setUp(self):
        """Set up a new CalculatorUIController instance before each test."""
        self.controller = CalculatorUIController()

    def test_evaluate_valid_expressions_with_spaces(self):
        """Test evaluation of valid expressions with spaces."""
        self.assertEqual(self.controller.evaluate("10 + 5"), 15.0)
        self.assertEqual(self.controller.evaluate("10 - 5"), 5.0)
        self.assertEqual(self.controller.evaluate("10 * 5"), 50.0)
        self.assertEqual(self.controller.evaluate("10 / 5"), 2.0)
        self.assertEqual(self.controller.evaluate("2 + 3 * 4"), 14.0) # Precedence
        self.assertEqual(self.controller.evaluate("10 - 4 / 2"), 8.0) # Precedence
        self.assertEqual(self.controller.evaluate("10 / 2 * 5"), 25.0) # Left-to-right for same precedence

    def test_evaluate_valid_expressions_without_spaces(self):
        """Test evaluation of valid expressions without spaces."""
        self.assertEqual(self.controller.evaluate("10+5"), 15.0)
        self.assertEqual(self.controller.evaluate("10-5"), 5.0)
        self.assertEqual(self.controller.evaluate("10*5"), 50.0)
        self.assertEqual(self.controller.evaluate("10/5"), 2.0)
        self.assertEqual(self.controller.evaluate("2+3*4"), 14.0)
        self.assertEqual(self.controller.evaluate("10-4/2"), 8.0)
        self.assertEqual(self.controller.evaluate("10/2*5"), 25.0)
        self.assertEqual(self.controller.evaluate("1.5+2.5"), 4.0)
        self.assertEqual(self.controller.evaluate("10.5*2"), 21.0)
        self.assertEqual(self.controller.evaluate("-5+3"), -2.0) # Unary minus at start
        self.assertEqual(self.controller.evaluate("5+-2"), 3.0) # Unary minus after operator
        self.assertEqual(self.controller.evaluate("5*-2"), -10.0) # Unary minus after operator
        self.assertEqual(self.controller.evaluate("10--5"), 15.0) # Double negative

    def test_evaluate_division_by_zero(self):
        """Test division by zero raises a ValueError."""
        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("10/0")
        self.assertEqual(str(cm.exception), "Arithmetic error: Cannot divide by zero")

        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("0/0")
        self.assertEqual(str(cm.exception), "Arithmetic error: Cannot divide by zero")

    def test_evaluate_invalid_expressions(self):
        """Test evaluation of invalid expressions."""
        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("abc")
        self.assertIn("Invalid expression format", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("10+")
        self.assertIn("ends with operator", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("+10")
        self.assertIn("starts with operator", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("10 * / 5")
        self.assertIn("consecutive operators", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("")
        self.assertEqual(str(cm.exception), "Expression cannot be empty.")

        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("10 5") # Consecutive numbers
        self.assertIn("consecutive numbers", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("--5") # Invalid unary minus usage
        self.assertIn("unary minus not followed by a number", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("5*-") # Invalid unary minus usage
        self.assertIn("unary minus not followed by a number", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            self.controller.evaluate("5+-") # Invalid unary minus usage
        self.assertIn("unary minus not followed by a number", str(cm.exception))
