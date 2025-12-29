import unittest
from hrishikeshs_calculator.calculator import Hrishikesh_Calculator

class TestHrishikeshCalculator(unittest.TestCase):
    """Unit tests for the Hrishikesh_Calculator class."""

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
        self.assertEqual(self.calculator.multiply(4, 6), 24)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(8, 4), 2)
        self.assertRaises(ValueError, self.calculator.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()