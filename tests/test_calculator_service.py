import pytest
from src.calculator.calculator_service import CalculatorService

@pytest.fixture
def service() -> CalculatorService:
    """Provides a CalculatorService instance for tests."""
    return CalculatorService()

def test_add(service: CalculatorService):
    """Test addition operation."""
    assert service.calculate(5, 3, "add") == 8
    assert service.calculate(-5, 3, "add") == -2
    assert service.calculate(0, 0, "add") == 0
    assert service.calculate(1.5, 2.5, "add") == 4.0

def test_subtract(service: CalculatorService):
    """Test subtraction operation."""
    assert service.calculate(5, 3, "subtract") == 2
    assert service.calculate(3, 5, "subtract") == -2
    assert service.calculate(0, 0, "subtract") == 0
    assert service.calculate(5.5, 1.5, "subtract") == 4.0

def test_multiply(service: CalculatorService):
    """Test multiplication operation."""
    assert service.calculate(5, 3, "multiply") == 15
    assert service.calculate(-5, 3, "multiply") == -15
    assert service.calculate(5, -3, "multiply") == -15
    assert service.calculate(0, 5, "multiply") == 0
    assert service.calculate(1.5, 2, "multiply") == 3.0

def test_divide(service: CalculatorService):
    """Test division operation."""
    assert service.calculate(6, 3, "divide") == 2
    assert service.calculate(-6, 3, "divide") == -2
    assert service.calculate(5, 2, "divide") == 2.5
    assert service.calculate(0, 5, "divide") == 0

def test_divide_by_zero(service: CalculatorService):
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        service.calculate(5, 0, "divide")
