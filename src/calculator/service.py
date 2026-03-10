def calculate(operand1: float, operand2: float, operation: str) -> float:
    """
    Performs a calculation based on the provided operands and operation.

    Args:
        operand1: The first number.
        operand2: The second number.
        operation: The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        The result of the calculation.

    Raises:
        ValueError: If the operation is invalid or division by zero occurs.
    """
    if operation == 'add':
        return operand1 + operand2
    elif operation == 'subtract':
        return operand1 - operand2
    elif operation == 'multiply':
        return operand1 * operand2
    elif operation == 'divide':
        if operand2 == 0:
            raise ValueError("Cannot divide by zero")
        return operand1 / operand2
    else:
        raise ValueError(f"Invalid operation: {operation}")
