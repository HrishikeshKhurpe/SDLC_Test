import logging
import re
from .calculator import Calculator # Import Calculator from its new location

class CalculatorUIController:
    """
    Controller for the calculator UI, handling expression evaluation logic.
    """

    def __init__(self):
        """
        Initializes the CalculatorUIController with a Calculator instance.
        """
        self.calculator = Calculator()

    def evaluate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression.

        Args:
            expression: The mathematical expression as a string (e.g., "10+5*2").

        Returns:
            The result of the evaluation as a float.

        Raises:
            ValueError: If the expression is invalid or division by zero occurs.
        """
        logging.info(f"Attempting to evaluate expression: '{expression}'")
        
        # Explicitly remove all spaces from the expression before tokenization
        expression = expression.replace(" ", "")

        if not expression:
            logging.warning("Attempted to evaluate an empty expression.")
            raise ValueError("Expression cannot be empty.")

        # Step 1: Tokenize the expression into raw numbers and operators
        # This regex captures numbers (integers or floats) and single-character operators.
        raw_tokens = re.findall(r'(\d+\.?\d*|[+\-*/])', expression)

        if not raw_tokens:
            logging.error(f"No valid tokens found in expression: '{expression}'")
            raise ValueError(f"Invalid expression format: '{expression}'")

        # Step 2: Process raw_tokens to handle unary minus
        processed_tokens = []
        i = 0
        while i < len(raw_tokens):
            token = raw_tokens[i]
            # Check for unary minus: '-' at the beginning or after an operator
            if token == '-' and (i == 0 or raw_tokens[i-1] in ['+', '-', '*', '/']):
                if i + 1 < len(raw_tokens) and re.match(r'^\d+\.?\d*$', raw_tokens[i+1]):
                    # It's a unary minus followed by a number, combine them
                    processed_tokens.append(float(token + raw_tokens[i+1]))
                    i += 1 # Skip the next token as it's already consumed
                else:
                    # Unary minus not followed by a valid number (e.g., "5*-", "--5")
                    logging.error(f"Invalid unary minus usage in expression: '{expression}' at token index {i}")
                    raise ValueError(f"Invalid expression: unary minus not followed by a number at '{expression[i:]}'")
            else:
                # Regular number or binary operator
                try:
                    # Try converting to float if it looks like a number
                    if re.match(r'^\d+\.?\d*$', token):
                        processed_tokens.append(float(token))
                    else:
                        processed_tokens.append(token) # It's an operator
                except ValueError:
                    logging.error(f"Invalid number format in token '{token}' for expression: '{expression}'")
                    raise ValueError(f"Invalid number format: '{token}' in expression: '{expression}'")
            i += 1

        if not processed_tokens:
            logging.error(f"No valid processed tokens after unary minus handling for expression: '{expression}'")
            raise ValueError(f"Invalid expression format: '{expression}'")

        # Basic validation: ensure tokens alternate between numbers and operators
        # and don't start/end with an operator (unless it's a negative number start, which is handled by processed_tokens)
        # Now, processed_tokens should start with a number (positive or negative)
        # and end with a number.
        if not isinstance(processed_tokens[0], (int, float)):
            logging.error(f"Expression starts with an invalid token: '{processed_tokens[0]}' in '{expression}'")
            raise ValueError(f"Invalid expression format: '{expression}' (starts with operator)")
        if not isinstance(processed_tokens[-1], (int, float)):
            logging.error(f"Expression ends with an invalid token: '{processed_tokens[-1]}' in '{expression}'")
            raise ValueError(f"Invalid expression format: '{expression}' (ends with operator)")

        # Check for consecutive operators or numbers
        for j in range(len(processed_tokens) - 1):
            current = processed_tokens[j]
            next_t = processed_tokens[j+1]
            if isinstance(current, (int, float)) and isinstance(next_t, (int, float)):
                logging.error(f"Consecutive numbers found in expression: '{expression}' at '{current}' and '{next_t}'")
                raise ValueError(f"Invalid expression format: '{expression}' (consecutive numbers)")
            if isinstance(current, str) and isinstance(next_t, str): # Both are operators
                logging.error(f"Consecutive operators found in expression: '{expression}' at '{current}' and '{next_t}'")
                raise ValueError(f"Invalid expression format: '{expression}' (consecutive operators)")

        # Convert tokens to a postfix (Reverse Polish Notation) expression using Shunting-yard algorithm
        output_queue = []
        operator_stack = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        for item in processed_tokens:
            if isinstance(item, float): # It's a number
                output_queue.append(item)
            elif item in precedence: # It's an operator
                while (operator_stack and operator_stack[-1] in precedence and
                       precedence[operator_stack[-1]] >= precedence[item]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(item)
            else:
                logging.error(f"Unrecognized item '{item}' in processed tokens for expression: '{expression}'")
                raise ValueError(f"Invalid token '{item}' in expression: '{expression}'")

        while operator_stack:
            output_queue.append(operator_stack.pop())

        # Evaluate the postfix expression
        operand_stack = []
        for item in output_queue:
            if isinstance(item, float):
                operand_stack.append(item)
            else: # It's an operator string
                if len(operand_stack) < 2:
                    logging.error(f"Insufficient operands for operator '{item}' in expression: '{expression}'")
                    raise ValueError(f"Invalid expression: '{expression}' (missing operand for '{item}')")
                
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()

                try:
                    if item == '+':
                        operand_stack.append(self.calculator.add(operand1, operand2))
                    elif item == '-':
                        operand_stack.append(self.calculator.subtract(operand1, operand2))
                    elif item == '*':
                        operand_stack.append(self.calculator.multiply(operand1, operand2))
                    elif item == '/':
                        operand_stack.append(self.calculator.divide(operand1, operand2))
                except ValueError as e: # Catch division by zero from Calculator
                    logging.error(f"Arithmetic error during evaluation: {e}")
                    raise ValueError(f"Arithmetic error: {e}") from e
                except Exception as e:
                    logging.critical(f"Unexpected error during arithmetic operation: {e}", exc_info=True)
                    raise ValueError(f"Unexpected error during calculation: {e}") from e

        if len(operand_stack) != 1:
            logging.error(f"Invalid expression: '{expression}' (malformed postfix expression, final stack size {len(operand_stack)})")
            raise ValueError(f"Invalid expression: '{expression}' (malformed expression)")

        result = operand_stack[0]
        logging.info(f"Expression '{expression}' evaluated to: {result}")
        return result
