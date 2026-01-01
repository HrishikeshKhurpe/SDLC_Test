import logging
from calculator.calculator import Hrishikesh_Calculator

class CalculatorUIController:
    def __init__(self):
        self.calculator = Hrishikesh_Calculator()
        
    def add(self, a, b):
        """Add two numbers."""
        try:
            return self.calculator.add(a, b)
        except ValueError as e:
            logging.error(f"Error adding {a} and {b}: {e}")
            raise
            
    def subtract(self, a, b):
        """Subtract two numbers."""
        try:
            return self.calculator.subtract(a, b)
        except ValueError as e:
            logging.error(f"Error subtracting {b} from {a}: {e}")
            raise
            
    def multiply(self, a, b):
        """Multiply two numbers."""
        try:
            return self.calculator.multiply(a, b)
        except ValueError as e:
            logging.error(f"Error multiplying {a} and {b}: {e}")
            raise
            
    def divide(self, a, b):
        """Divide two numbers."""
        try:
            return self.calculator.divide(a, b)
        except ValueError as e:
            logging.error(f"Error dividing {a} by {b}: {e}")
            raise
            
    def evaluate(self, expression):
        """Evaluate the given expression."""
        try:
            parts = expression.split()
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])
            
            if operator == "+":
                return self.add(a, b)
            elif operator == "-":
                return self.subtract(a, b)
            elif operator == "*":
                return self.multiply(a, b)
            elif operator == "/":
                return self.divide(a, b)
            else:
                raise ValueError(f"Invalid operator: {operator}")
        except (ValueError, IndexError) as e:
            logging.error(f"Error evaluating expression: {expression}, {e}")
            raise ValueError("Invalid expression format.") from e
