import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

class Hrishikesh_Calculator:
    """A simple calculator that supports basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        try:
            result = a + b
            logging.info(f"Adding {a} and {b}, result: {result}")
            return result
        except Exception as e:
            logging.error(f"Error in addition: {e}")
            raise e

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers."""
        try:
            result = a - b
            logging.info(f"Subtracting {b} from {a}, result: {result}")
            return result
        except Exception as e:
            logging.error(f"Error in subtraction: {e}")
            raise e

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        try:
            result = a * b
            logging.info(f"Multiplying {a} and {b}, result: {result}")
            return result
        except Exception as e:
            logging.error(f"Error in multiplication: {e}")
            raise e

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers."""
        try:
            if b == 0:
                raise ValueError("Cannot divide by zero")
            result = a / b
            logging.info(f"Dividing {a} by {b}, result: {result}")
            return result
        except ZeroDivisionError:
            logging.error("Error: Division by zero")
            raise
        except Exception as e:
            logging.error(f"Error in division: {e}")
            raise e

if __name__ == "__main__":
    calc = Hrishikesh_Calculator()
    print(calc.add(5, 3))  # Output: 8.0
    print(calc.subtract(10, 4))  # Output: 6.0
    print(calc.multiply(4, 6))  # Output: 24.0
    print(calc.divide(10, 2))  # Output: 5.0
    print(calc.divide(10, 0))  # Raises ZeroDivisionError