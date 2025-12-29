""
import logging

class Hrishikesh_Calculator:
    """
    A simple calculator that supports basic arithmetic operations.
    """
    def __init__(self):
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
        self.logger.debug(f"Adding {a} and {b}")
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
        self.logger.debug(f"Subtracting {b} from {a}")
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
        self.logger.debug(f"Multiplying {a} and {b}")
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
        self.logger.debug(f"Dividing {a} by {b}")
        if b == 0:
            self.logger.error("Cannot divide by zero")
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    ""