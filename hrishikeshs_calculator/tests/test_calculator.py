import unittest
from hrishikeshs_calculator.calculator import Hrishikesh_Calculator

class TestHrishikeshCalculator(unittest.TestCase):
    """
    Test cases for the Hrishikesh_Calculator class.
    """
    def setUp(self):
        self.calculator = Hrishikesh_Calculator()
    
    def test_add(self):
        """
        Test the add method.
        """
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-2, 3), 1)
        self.assertEqual(self.calculator.add(0, 0), 0)
        
        with self.assertRaises(TypeError):
            self.calculator.add("a", 3)
            self.calculator.add(2, "b")
    
    def test_subtract(self):
        """
        Test the subtract method.
        """
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(-2, 3), -5)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        
        with self.assertRaises(TypeError):
            self.calculator.subtract("a", 3)
            self.calculator.subtract(2, "b")
    
    def test_multiply(self):
        """
        Test the multiply method.
        """
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 0), 0)
        
        with self.assertRaises(TypeError):
            self.calculator.multiply("a", 3)
            self.calculator.multiply(2, "b")
    
    def test_divide(self):
        """
        Test the divide method.
        """
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(-6, 3), -2)
        self.assertEqual(self.calculator.divide(0, 1), 0)
        
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(6, 0)
        
        with self.assertRaises(TypeError):
            self.calculator.divide("a", 3)
            self.calculator.divide(2, "b")