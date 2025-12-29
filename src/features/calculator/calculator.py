class Hrishikesh_Calculator:
    """Performs basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers."""
        try:
            return a + b
        except (TypeError, ValueError) as e:
            logging.error(f"Error adding {a} and {b}: {e}")
            raise ValueError("Invalid input for addition. Please provide numeric values.") from e

    def subtract(self, a, b):
        """Subtract two numbers."""
        try:
            return a - b
        except (TypeError, ValueError) as e:
            logging.error(f"Error subtracting {b} from {a}: {e}")
            raise ValueError("Invalid input for subtraction. Please provide numeric values.") from e

    def multiply(self, a, b):
        """Multiply two numbers."""
        try:
            return a * b
        except (TypeError, ValueError) as e:
            logging.error(f"Error multiplying {a} and {b}: {e}")
            raise ValueError("Invalid input for multiplication. Please provide numeric values.") from e

    def divide(self, a, b):
        """Divide two numbers."""
        try:
            return a / b
        except (TypeError, ValueError, ZeroDivisionError) as e:
            logging.error(f"Error dividing {a} by {b}: {e}")
            if b == 0:
                raise ValueError("Cannot divide by zero.") from e
            else:
                raise ValueError("Invalid input for division. Please provide numeric values.") from e