import logging

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    """

    def add(self, x: float, y: float) -> float:
        """Adds two numbers."""
        logging.info(f"Adding {x} and {y}")
        return x + y

    def subtract(self, x: float, y: float) -> float:
        """Subtracts the second number from the first."""
        logging.info(f"Subtracting {y} from {x}")
        return x - y

    def multiply(self, x: float, y: float) -> float:
        """Multiplies two numbers."""
        logging.info(f"Multiplying {x} by {y}")
        return x * y

    def divide(self, x: float, y: float) -> float:
        """Divides the first number by the second. Raises ValueError if dividing by zero."""
        logging.info(f"Dividing {x} by {y}")
        if y == 0:
            logging.error("Attempted to divide by zero")
            raise ValueError("Cannot divide by zero")
        return x / y
