class Hrishikesh_Calculator:
    """
    A simple calculator that supports basic arithmetic operations.
    """
    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a (float): The first number to add.
            b (float): The second number to add.
        
        Returns:
            float: The sum of the two numbers.
        """
        try:
            return a + b
        except TypeError as e:
            print(f"Error adding numbers: {e}")
            raise e
        
    def subtract(self, a, b):
        """
        Subtract two numbers.
        
        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.
        
        Returns:
            float: The difference between the two numbers.
        """
        try:
            return a - b
        except TypeError as e:
            print(f"Error subtracting numbers: {e}")
            raise e
        
    def multiply(self, a, b):
        """
        Multiply two numbers.
        
        Args:
            a (float): The first number to multiply.
            b (float): The second number to multiply.
        
        Returns:
            float: The product of the two numbers.
        """
        try:
            return a * b
        except TypeError as e:
            print(f"Error multiplying numbers: {e}")
            raise e
        
    def divide(self, a, b):
        """
        Divide two numbers.
        
        Args:
            a (float): The number to divide.
            b (float): The number to divide by.
        
        Returns:
            float: The quotient of the two numbers.
        
        Raises:
            ZeroDivisionError: If the divisor (b) is zero.
        """
        try:
            return a / b
        except ZeroDivisionError as e:
            print(f"Error dividing numbers: {e}")
            raise e
        except TypeError as e:
            print(f"Error dividing numbers: {e}")
            raise e