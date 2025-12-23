""
import unittest
from src.features.calculator.calculator import Hrishikesh_Calculator

class TestHrishikeshCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Hrishikesh_Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(-2, 4), 2)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 4), 6)
        self.assertEqual(self.calculator.subtract(0, 5), -5)
        self.assertEqual(self.calculator.subtract(7, 7), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 6), 12)
        self.assertEqual(self.calculator.multiply(-3, 4), -12)
        self.assertEqual(self.calculator.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(15, 3), 5)
        self.assertEqual(self.calculator.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
""