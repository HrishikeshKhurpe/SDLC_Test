import logging

class InputValidator:
    """Provides input validation utilities for the calculator."""

    @staticmethod
    def validate_number(value):
        """Validate that the input is a valid number."""
        try:
            return float(value)
        except (ValueError, TypeError) as e:
            logging.error(f"Error validating input '{value}': {e}")
            raise ValueError("Invalid input. Please provide a valid number.") from e

    @staticmethod
    def validate_operator(operator):
        """Validate that the input is a valid arithmetic operator."""
        valid_operators = ['+', '-', '*', '/']
        if operator not in valid_operators:
            logging.error(f"Invalid operator: '{operator}'.")
            raise ValueError(f"Invalid operator: '{operator}'. Please use one of the valid operators: {', '.join(valid_operators)}")
        return operator

class ErrorHandler:
    """Provides error handling utilities for the calculator."""

    @staticmethod
    def handle_value_error(func):
        """Decorator to handle ValueError exceptions."""
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                logging.error(str(e))
                raise
        return wrapper

    @staticmethod
    def handle_zero_division_error(func):
        """Decorator to handle ZeroDivisionError exceptions."""
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ZeroDivisionError as e:
                logging.error(str(e))
                raise ValueError("Cannot divide by zero.") from e
        return wrapper