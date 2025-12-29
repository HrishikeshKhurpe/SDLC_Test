""
import unittest
from calculator.calculator import Hrishikesh_Calculator

class TestHrishikeshCalculator(unittest.TestCase):
    """
    Unit tests for the Hrishikesh_Calculator class.
    """
    def setUp(self):
        self.calculator = Hrishikesh_Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 2), -2)
        self.assertEqual(self.calculator.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(4, 2), 2)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)
    ""