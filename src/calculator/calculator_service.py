import operator
from typing import Dict, Callable

class CalculatorService:
    """
    A service to perform calculator operations.
    """
    def __init__(self):
        self._operations: Dict[str, Callable[[float, float], float]] = {
            "add": operator.add,
            "subtract": operator.sub,
            "multiply": operator.mul,
            "divide": operator.truediv,
        }

    def calculate(self, number1: float, number2: float, operation: str) -> float:
        """
        Performs a calculation based on the provided numbers and operation.

        Args:
            number1: The first number.
            number2: The second number.
            operation: The operation to perform ('add', 'subtract', 'multiply', 'divide').

        Returns:
            The result of the calculation.

        Raises:
            ValueError: If division by zero is attempted.
        """
        if operation == "divide" and number2 == 0:
            raise ValueError("Division by zero is not allowed.")

        # The operation is guaranteed to be valid by the DTO/Pydantic model
        op_func = self._operations[operation]
        return op_func(number1, number2)
