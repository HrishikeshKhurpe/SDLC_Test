import unittest
from unittest.mock import patch
from calculator.ui import CalculatorUI
from calculator.ui_controller import CalculatorUIController

class TestCalculatorUI(unittest.TestCase):
    def setUp(self):
        self.ui = CalculatorUI()
        self.controller = CalculatorUIController()

    @patch('calculator.ui.Hrishikesh_Calculator')
    def test_add(self, mock_calculator):
        mock_calculator.return_value.add.return_value = 5
        self.ui.add_to_display("2")
        self.ui.add_to_display("+")
        self.ui.add_to_display("3")
        self.ui.evaluate()
        self.assertEqual(self.ui.display.get(), "5")

    @patch('calculator.ui.Hrishikesh_Calculator')
    def test_subtract(self, mock_calculator):
        mock_calculator.return_value.subtract.return_value = 2
        self.ui.add_to_display("5")
        self.ui.add_to_display("-")
        self.ui.add_to_display("3")
        self.ui.evaluate()
        self.assertEqual(self.ui.display.get(), "2")

    @patch('calculator.ui.Hrishikesh_Calculator')
    def test_multiply(self, mock_calculator):
        mock_calculator.return_value.multiply.return_value = 6
        self.ui.add_to_display("2")
        self.ui.add_to_display("*")
        self.ui.add_to_display("3")
        self.ui.evaluate()
        self.assertEqual(self.ui.display.get(), "6")

    @patch('calculator.ui.Hrishikesh_Calculator')
    def test_divide(self, mock_calculator):
        mock_calculator.return_value.divide.return_value = 2.0
        self.ui.add_to_display("6")
        self.ui.add_to_display("/")
        self.ui.add_to_display("3")
        self.ui.evaluate()
        self.assertEqual(self.ui.display.get(), "2.0")

    @patch('calculator.ui.Hrishikesh_Calculator')
    def test_error_handling(self, mock_calculator):
        mock_calculator.return_value.add.side_effect = ValueError("Invalid input types")
        self.ui.add_to_display("a")
        self.ui.add_to_display("+")
        self.ui.add_to_display("b")
        self.ui.evaluate()
        self.assertEqual(self.ui.display.get(), "Error")

if __name__ == '__main__':
    unittest.main()