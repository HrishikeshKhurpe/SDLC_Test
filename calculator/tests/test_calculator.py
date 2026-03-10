import unittest
import sys
import os

# Add the parent directory to sys.path to allow importing modules from 'calculator'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator.calculator import Calculator
from calculator.ui_controller import UIController

class TestCalculator(unittest.TestCase):
    """
    Unit tests for the Calculator class.
    """
    def setUp(self):
        """
        Set up a new Calculator instance before each test.
        """
        self.calculator = Calculator()

    def test_add(self):
        """
        Test the addition operation.
        """
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertAlmostEqual(self.calculator.add(2.5, 3.5), 6.0)

    def test_subtract(self):
        """
        Test the subtraction operation.
        """
        self.assertEqual(self.calculator.subtract(5, 2), 3)
        self.assertEqual(self.calculator.subtract(2, 5), -3)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertAlmostEqual(self.calculator.subtract(5.5, 2.5), 3.0)

    def test_multiply(self):
        """
        Test the multiplication operation.
        """
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)
        self.assertEqual(self.calculator.multiply(0, 10), 0)
        self.assertAlmostEqual(self.calculator.multiply(2.5, 2), 5.0)

    def test_divide(self):
        """
        Test the division operation.
        """
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(10, 4), 2.5)
        self.assertAlmostEqual(self.calculator.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """
        Test division by zero raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

class TestCalculatorUIController(unittest.TestCase):
    """
    Unit tests for the UIController class's evaluate method.
    """
    def setUp(self):
        """
        Set up a new UIController instance with a Calculator before each test.
        """
        self.calculator = Calculator()
        self.controller = UIController(self.calculator)

    def test_basic_operations(self):
        """
        Test basic arithmetic operations.
        """
        self.assertAlmostEqual(self.controller.evaluate("2+3"), 5.0)
        self.assertAlmostEqual(self.controller.evaluate("5-2"), 3.0)
        self.assertAlmostEqual(self.controller.evaluate("2*3"), 6.0)
        self.assertAlmostEqual(self.controller.evaluate("6/3"), 2.0)
        self.assertAlmostEqual(self.controller.evaluate("10/4"), 2.5)

    def test_operator_precedence(self):
        """
        Test expressions with operator precedence.
        """
        self.assertAlmostEqual(self.controller.evaluate("2+3*4"), 14.0)
        self.assertAlmostEqual(self.controller.evaluate("10-4/2"), 8.0)
        self.assertAlmostEqual(self.controller.evaluate("5*2+1"), 11.0)
        self.assertAlmostEqual(self.controller.evaluate("12/3-1"), 3.0)

    def test_parentheses(self):
        """
        Test expressions with parentheses.
        """
        self.assertAlmostEqual(self.controller.evaluate("(2+3)*4"), 20.0)
        self.assertAlmostEqual(self.controller.evaluate("10/(4-2)"), 5.0)
        self.assertAlmostEqual(self.controller.evaluate("(5+1)*(2+3)"), 30.0)
        self.assertAlmostEqual(self.controller.evaluate("((1+2)*3)/3"), 3.0)

    def test_unary_minus(self):
        """
        Test expressions with unary minus.
        """
        self.assertAlmostEqual(self.controller.evaluate("-5"), -5.0)
        self.assertAlmostEqual(self.controller.evaluate("10*-2"), -20.0)
        self.assertAlmostEqual(self.controller.evaluate("5+-3"), 2.0)
        self.assertAlmostEqual(self.controller.evaluate("-(2+3)"), -5.0) # Critical bug fix test
        self.assertAlmostEqual(self.controller.evaluate("-(-5)"), 5.0)
        self.assertAlmostEqual(self.controller.evaluate("10+(-(2*3))"), 4.0)

    def test_decimals(self):
        """
        Test expressions with decimal numbers.
        """
        self.assertAlmostEqual(self.controller.evaluate("2.5+3.5"), 6.0)
        self.assertAlmostEqual(self.controller.evaluate("10.0/4.0"), 2.5)
        self.assertAlmostEqual(self.controller.evaluate("1.5*2.0+0.5"), 3.5)

    def test_mixed_operations(self):
        """
        Test complex expressions with mixed operations, precedence, and parentheses.
        """
        self.assertAlmostEqual(self.controller.evaluate("3+4*2/(1-5)"), 1.0)
        self.assertAlmostEqual(self.controller.evaluate("5*(2+3)-10/2"), 20.0)
        self.assertAlmostEqual(self.controller.evaluate("((10+2)*3)/6-1"), 5.0)
        self.assertAlmostEqual(self.controller.evaluate("2.5 * (4 - 2) + 1"), 6.0)

    def test_division_by_zero_in_expression(self):
        """
        Test division by zero within an expression raises a ValueError.
        """
        with self.assertRaisesRegex(ValueError, "Division by zero is not allowed."):
            self.controller.evaluate("10/0")
        with self.assertRaisesRegex(ValueError, "Division by zero is not allowed."):
            self.controller.evaluate("5/(3-3)")
        with self.assertRaisesRegex(ValueError, "Division by zero is not allowed."):
            self.controller.evaluate("1+2*3/0")

    def test_empty_expression(self):
        """
        Test evaluating an empty expression raises a ValueError.
        """
        with self.assertRaisesRegex(ValueError, "Expression cannot be empty."):
            self.controller.evaluate("")

    def test_invalid_tokens(self):
        """
        Test expressions with invalid tokens raise a ValueError.
        """
        with self.assertRaisesRegex(ValueError, "Invalid token in expression: @"):
            self.controller.evaluate("2+3@4")
        with self.assertRaisesRegex(ValueError, "Invalid token in expression: a"):
            self.controller.evaluate("10a5")

    def test_mismatched_parentheses(self):
        """
        Test expressions with mismatched parentheses raise a ValueError.
        """
        with self.assertRaisesRegex(ValueError, "Mismatched parentheses."):
            self.controller.evaluate("(2+3")
        with self.assertRaisesRegex(ValueError, "Mismatched parentheses."):
            self.controller.evaluate("2+3)")
        with self.assertRaisesRegex(ValueError, "Mismatched parentheses."):
            self.controller.evaluate("((2+3)")

    def test_unary_minus_invalid_follow(self):
        """
        Test unary minus followed by invalid token raises a ValueError.
        """
        with self.assertRaisesRegex(ValueError, "Unary minus must be followed by a number or an opening parenthesis."):
            self.controller.evaluate("-*5")
        with self.assertRaisesRegex(ValueError, "Unary minus must be followed by a number or an opening parenthesis."):
            self.controller.evaluate("-+")
        with self.assertRaisesRegex(ValueError, "Unary minus must be followed by a number or an opening parenthesis."):
            self.controller.evaluate("-") # Unary minus at end of expression

    def test_complex_unary_minus_and_parentheses(self):
        """
        Test complex scenarios involving unary minus and nested parentheses.
        """
        self.assertAlmostEqual(self.controller.evaluate("-(2*(-3+5))"), -4.0)
        self.assertAlmostEqual(self.controller.evaluate("10 - (-5)"), 15.0)
        self.assertAlmostEqual(self.controller.evaluate("10 + (- (2 + 3))"), 5.0)
        self.assertAlmostEqual(self.controller.evaluate("-(10/2)"), -5.0)
        self.assertAlmostEqual(self.controller.evaluate("(-2)*(-3)"), 6.0)
        self.assertAlmostEqual(self.controller.evaluate("(-2)+(-3)"), -5.0)

    def test_multiple_unary_minus(self):
        """
        Test expressions with multiple unary minus operators.
        """
        self.assertAlmostEqual(self.controller.evaluate("--5"), 5.0) # --5 is equivalent to -(-5)
        self.assertAlmostEqual(self.controller.evaluate("---5"), -5.0)
        self.assertAlmostEqual(self.controller.evaluate("10 + ---5"), 5.0)
        self.assertAlmostEqual(self.controller.evaluate("10 - --5"), 5.0)

if __name__ == '__main__':
    unittest.main()
