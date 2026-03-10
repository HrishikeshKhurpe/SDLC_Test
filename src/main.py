import logging
from typing import Dict, Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

class CalculationRequest(BaseModel):
    operand1: Union[int, float]
    operand2: Union[int, float]
    operation: str

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Adds two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtracts the second number from the first.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference between a and b.
    """
    return a - b

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiplies two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b

def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divides the first number by the second.

    Args:
        a: The numerator.
        b: The denominator.

    Raises:
        ValueError: If the denominator (b) is zero.

    Returns:
        The quotient of a and b.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

@app.post("/calculate")
def calculate(request: CalculationRequest) -> Dict[str, Union[int, float, str]]:
    """
    Performs a calculation based on the request body.

    The endpoint expects a JSON object with two numbers (`operand1`, `operand2`)
    and an operation string.

    Args:
        request: A `CalculationRequest` object containing two operands and an operation.

    Raises:
        HTTPException: 400 for invalid operations or division by zero.

    Returns:
        A dictionary containing the result of the calculation.
    """
    logging.info(f"Received calculation request: {request.operation} {request.operand1} and {request.operand2}")
    op_func = operations.get(request.operation)
    if not op_func:
        supported_ops = sorted(operations.keys())
        error_msg = f"Invalid operation '{request.operation}'. Supported operations are: {', '.join(supported_ops)}"
        logging.error(error_msg)
        raise HTTPException(status_code=400, detail=error_msg)

    try:
        result = op_func(request.operand1, request.operand2)
        logging.info(f"Calculation successful: {request.operand1} {request.operation} {request.operand2} = {result}")
        return {"result": result}
    except ValueError as e:
        logging.error(f"Error during calculation: {e}")
        raise HTTPException(status_code=400, detail=str(e))
