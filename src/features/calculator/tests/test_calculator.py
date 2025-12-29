import unittest
from src.features.calculator.calculator import Hrishikesh_Calculator

class TestHrishikeshCalculator(unittest.TestCase):
    """Tests for the Hrishikesh_Calculator class."""

    def setUp(self):
        self.calculator = Hrishikesh_Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertRaises(ValueError, self.calculator.add, "a", 3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertRaises(ValueError, self.calculator.subtract, "a", 3)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 2), -2)
        self.assertRaises(ValueError, self.calculator.multiply, "a", 3)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(4, 2), 2)
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 4, 0)
        self.assertRaises(ValueError, self.calculator.divide, "a", 3)

if __name__ == '__main__':
    unittest.main()