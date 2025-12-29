import unittest
from calculator.calculator import Hrishikesh_Calculator

class TestHrishikeshCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Hrishikesh_Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-2, 3), 1)
        self.assertEqual(self.calculator.add(0, 0), 0)
        with self.assertRaises(ValueError):
            self.calculator.add("a", 3)
        with self.assertRaises(ValueError):
            self.calculator.add(2, "b")

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(3, 5), -2)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        with self.assertRaises(ValueError):
            self.calculator.subtract("a", 3)
        with self.assertRaises(ValueError):
            self.calculator.subtract(2, "b")

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 0), 0)
        with self.assertRaises(ValueError):
            self.calculator.multiply("a", 3)
        with self.assertRaises(ValueError):
            self.calculator.multiply(2, "b")

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2.0)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calculator.divide(6, 0)
        with self.assertRaises(ValueError):
            self.calculator.divide("a", 3)
        with self.assertRaises(ValueError):
            self.calculator.divide(2, "b")