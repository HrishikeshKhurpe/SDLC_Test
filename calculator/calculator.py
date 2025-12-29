class Hrishikesh_Calculator:
    """Performs basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers."""
        try:
            return a + b
        except TypeError as e:
            logging.error(f"Error adding {a} and {b}: {e}")
            raise ValueError("Invalid input types. Please provide numbers.") from e

    def subtract(self, a, b):
        """Subtract two numbers."""
        try:
            return a - b
        except TypeError as e:
            logging.error(f"Error subtracting {b} from {a}: {e}")
            raise ValueError("Invalid input types. Please provide numbers.") from e

    def multiply(self, a, b):
        """Multiply two numbers."""
        try:
            return a * b
        except TypeError as e:
            logging.error(f"Error multiplying {a} and {b}: {e}")
            raise ValueError("Invalid input types. Please provide numbers.") from e

    def divide(self, a, b):
        """Divide two numbers."""
        try:
            return a / b
        except TypeError as e:
            logging.error(f"Error dividing {a} by {b}: {e}")
            raise ValueError("Invalid input types. Please provide numbers.") from e
        except ZeroDivisionError as e:
            logging.error(f"Error dividing {a} by {b}: {e}")
            raise ValueError("Cannot divide by zero.") from e