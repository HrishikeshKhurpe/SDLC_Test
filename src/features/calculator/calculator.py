""
import logging

class Hrishikesh_Calculator:
    """
    Hrishikesh's Calculator class that supports basic arithmetic operations.
    """
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.

        Args:
            a (float): The first number to add.
            b (float): The second number to add.

        Returns:
            float: The sum of the two numbers.
        """
        self.logger.info(f"Adding {a} and {b}")
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtract two numbers.

        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.

        Returns:
            float: The difference between the two numbers.
        """
        self.logger.info(f"Subtracting {b} from {a}")
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a (float): The first number to multiply.
            b (float): The second number to multiply.

        Returns:
            float: The product of the two numbers.
        """
        self.logger.info(f"Multiplying {a} and {b}")
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divide two numbers.

        Args:
            a (float): The number to divide.
            b (float): The number to divide by.

        Returns:
            float: The quotient of the two numbers.

        Raises:
            ZeroDivisionError: If the second argument is zero.
        """
        self.logger.info(f"Dividing {a} by {b}")
        if b == 0:
            self.logger.error("Cannot divide by zero")
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
"""
Example usage:
calculator = Hrishikesh_Calculator()
print(calculator.add(5, 3))  # Output: 8.0
print(calculator.subtract(10, 4))  # Output: 6.0
print(calculator.multiply(2, 6))  # Output: 12.0
print(calculator.divide(15, 3))  # Output: 5.0
"""
