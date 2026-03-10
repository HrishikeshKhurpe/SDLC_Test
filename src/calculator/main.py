from fastapi import FastAPI, HTTPException, status
from .dtos import CalculatorRequest, CalculatorResponse
from .calculator_service import CalculatorService

app = FastAPI(
    title="Calculator API",
    description="A simple REST API for a calculator.",
    version="1.0.0",
)

# In a real application, this might be managed with a dependency injection container
calculator_service = CalculatorService()

@app.get("/", tags=["Health Check"], summary="Health check endpoint")
def read_root():
    """
    A simple health check endpoint to confirm the API is running.
    """
    return {"status": "ok"}

@app.post(
    "/calculator",
    response_model=CalculatorResponse,
    tags=["Calculator"],
    summary="Perform a calculation",
)
def calculate(request: CalculatorRequest):
    """
    Performs a calculation based on two numbers and an operation.

    - **number1**: The first number (float).
    - **number2**: The second number (float).
    - **operation**: The operation to perform. Must be one of `add`, `subtract`, `multiply`, `divide`.
    """
    try:
        result = calculator_service.calculate(
            number1=request.number1,
            number2=request.number2,
            operation=request.operation,
        )
        return CalculatorResponse(result=result)
    except ValueError as e:
        # Handles division by zero
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except Exception:
        # Generic error handler for any other unexpected errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected internal error occurred.",
        )
