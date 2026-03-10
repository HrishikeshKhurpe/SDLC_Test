from pydantic import BaseModel, Field
from typing import Literal

class CalculatorRequest(BaseModel):
    number1: float
    number2: float
    operation: Literal["add", "subtract", "multiply", "divide"] = Field(
        ...,
        description="The operation to perform."
    )

class CalculatorResponse(BaseModel):
    result: float

class ErrorResponse(BaseModel):
    detail: str
