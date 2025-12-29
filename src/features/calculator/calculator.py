class Hrishikesh_Calculator:
    """Provides basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Adds two numbers."""
        try:
            return a + b
        except TypeError as e:
            logging.error(f"Error adding {a} and {b}: {e}")
            raise ValueError("Input must be numbers") from e

    def subtract(self, a: float, b: float) -> float:
        """Subtracts two numbers."""
        try:
            return a - b
        except TypeError as e:
            logging.error(f"Error subtracting {b} from {a}: {e}")
            raise ValueError("Input must be numbers") from e

    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers."""
        try:
            return a * b
        except TypeError as e:
            logging.error(f"Error multiplying {a} and {b}: {e}")
            raise ValueError("Input must be numbers") from e

    def divide(self, a: float, b: float) -> float:
        """Divides two numbers."""
        try:
            if b == 0:
                logging.error(f"Error dividing {a} by {b}: Division by zero")
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        except TypeError as e:
            logging.error(f"Error dividing {a} by {b}: {e}")
            raise ValueError("Input must be numbers") from e
