Here is the production-ready code for the calculator application:

{
  "files": [
    {
      "file_path": "hrishikesh_calculator/calculator.py",
      "content": """
import logging

logger = logging.getLogger(__name__)

class Calculator:
    """
    A simple calculator that supports basic arithmetic operations.
    """

    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.

        Args:
            a (float): The first number to add.
            b (float): The second number to add.

        Returns:
            float: The sum of the two numbers.

        Raises:
            TypeError: If either input is not a number.
        """
        logger.info(f"Adding {a} and {b}")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logger.error("Invalid input types for addition")
            raise TypeError("Both inputs must be numbers")
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtract two numbers.

        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.

        Returns:
            float: The difference between the two numbers.

        Raises:
            TypeError: If either input is not a number.
        """
        logger.info(f"Subtracting {b} from {a}")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logger.error("Invalid input types for subtraction")
            raise TypeError("Both inputs must be numbers")
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a (float): The first number to multiply.
            b (float): The second number to multiply.

        Returns:
            float: The product of the two numbers.

        Raises:
            TypeError: If either input is not a number.
        """
        logger.info(f"Multiplying {a} and {b}")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logger.error("Invalid input types for multiplication")
            raise TypeError("Both inputs must be numbers")
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divide two numbers.

        Args:
            a (float): The number to divide.
            b (float): The number to divide by.

        Returns:
            float: The quotient of the division.

        Raises:
            TypeError: If either input is not a number.
            ZeroDivisionError: If the second number is zero.
        """
        logger.info(f"Dividing {a} by {b}")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            logger.error("Invalid input types for division")
            raise TypeError("Both inputs must be numbers")
        if b == 0:
            logger.error("Division by zero")
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
",
      "change_type": "create",
      "explanation": "Implement the core calculator functionality, including addition, subtraction, multiplication, and division operations.",
      "dependencies": [],
      "callers_affected": [],
      "backward_compatible": true,
      "test_updates_required": ["tests/test_calculator.py"],
      "documentation_updates": ["README.md"]
    },
    {
      "file_path": "hrishikesh_calculator/cli.py",
      "content": """
import logging
from hrishikesh_calculator.calculator import Calculator

logger = logging.getLogger(__name__)

def main():
    """
    The main entry point for the calculator CLI.
    """
    calculator = Calculator()

    while True:
        try:
            print("Welcome to Hrishikesh's Calculator!")
            print("Please select an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "5":
                print("Exiting calculator...")
                break

            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            if choice == "1":
                result = calculator.add(a, b)
                print(f"The result is: {result}")
            elif choice == "2":
                result = calculator.subtract(a, b)
                print(f"The result is: {result}")
            elif choice == "3":
                result = calculator.multiply(a, b)
                print(f"The result is: {result}")
            elif choice == "4":
                result = calculator.divide(a, b)
                print(f"The result is: {result}")
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            logger.error("Invalid input. Please enter numbers only.")
            print("Error: Invalid input. Please enter numbers only.")
        except TypeError as e:
            logger.error(str(e))
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            logger.error(str(e))
            print(f"Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            print(f"Error: Unexpected error occurred. Please try again.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
",
      "change_type": "create",
      "explanation": "Implement the command-line interface for the calculator, allowing users to interact with the calculator through the terminal.",
      "dependencies": ["hrishikesh_calculator/calculator.py"],
      "callers_affected": [],
      "backward_compatible": true,
      "test_updates_required": ["tests/test_cli.py"],
      "documentation_updates": ["README.md"]
    }
  ],
  "readme": {
    "file_path": "README.md",
    "content": """
# Hrishikesh's Calculator

Hrishikesh's Calculator is a simple command-line calculator application that supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/HrishikeshKhurpe/SDLC_Test.git
   ```
2. Change to the project directory:
   ```
   cd SDLC_Test
   ```
3. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the calculator, execute the following command:

```
python hrishikesh_calculator/cli.py
```

This will start the calculator CLI, where you can perform the following operations:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Simply follow the on-screen prompts to use the calculator.

## API Documentation

The calculator functionality is implemented in the `hrishikesh_calculator/calculator.py` module. The following methods are available:

- `add(a: float, b: float) -> float`: Add two numbers.
- `subtract(a: float, b: float) -> float`: Subtract two numbers.
- `multiply(a: float, b: float) -> float`: Multiply two numbers.
- `divide(a: float, b: float) -> float`: Divide two numbers.

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and add appropriate tests.
4. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](