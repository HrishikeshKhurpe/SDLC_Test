import re
import logging
from calculator.calculator import Calculator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UIController:
    """
    Controller for the calculator UI, handling expression evaluation.
    """
    def __init__(self, calculator: Calculator):
        """
        Initializes the UIController with a Calculator instance.

        Args:
            calculator: An instance of the Calculator class for performing arithmetic operations.
        """
        self.calculator = calculator
        self.operators = {
            '+': {'precedence': 1, 'associativity': 'left'},
            '-': {'precedence': 1, 'associativity': 'left'},
            '*': {'precedence': 2, 'associativity': 'left'},
            '/': {'precedence': 2, 'associativity': 'left'},
            '_UNARY_MINUS': {'precedence': 3, 'associativity': 'right'} # Special token for unary minus
        }

    def _apply_operator(self, operator: str, operand1: float, operand2: float = None) -> float:
        """
        Applies a given operator to one or two operands.

        Args:
            operator: The operator to apply (+, -, *, /, _UNARY_MINUS).
            operand1: The first operand.
            operand2: The second operand (optional, for binary operators).

        Returns:
            The result of the operation.

        Raises:
            ValueError: If an unknown operator is encountered or for division by zero.
        """
        if operator == '+':
            return self.calculator.add(operand1, operand2)
        elif operator == '-':
            return self.calculator.subtract(operand1, operand2)
        elif operator == '*':
            return self.calculator.multiply(operand1, operand2)
        elif operator == '/':
            if operand2 == 0:
                logging.error("Attempted division by zero.")
                raise ValueError("Division by zero is not allowed.")
            return self.calculator.divide(operand1, operand2)
        elif operator == '_UNARY_MINUS':
            return self.calculator.multiply(operand1, -1) # Apply negation
        else:
            logging.error(f"Unknown operator encountered: {operator}")
            raise ValueError(f"Unknown operator: {operator}")

    def evaluate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression using a shunting-yard-like algorithm.

        Supports basic arithmetic operations (+, -, *, /), parentheses, and unary minus.

        Args:
            expression: The mathematical expression string to evaluate.

        Returns:
            The numerical result of the expression.

        Raises:
            ValueError: If the expression is invalid (e.g., syntax error, division by zero).
        """
        if not expression:
            logging.warning("Attempted to evaluate an empty expression.")
            raise ValueError("Expression cannot be empty.")

        # Tokenization: Split numbers, operators, and parentheses
        # Use regex to split by operators and parentheses, keeping them as tokens
        # Also handle decimal numbers
        raw_tokens = re.findall(r'(\d+\.\d+|\d+|[+\-*/()])', expression.replace(' ', ''))
        logging.debug(f"Raw tokens: {raw_tokens}")

        # Process tokens for unary minus
        processed_tokens = []
        i = 0
        while i < len(raw_tokens):
            token = raw_tokens[i]
            if token == '-' and \
               (i == 0 or raw_tokens[i-1] in ['(', '+', '-', '*', '/']):
                # This is a unary minus
                # Check if the next token is a number or an opening parenthesis
                if i + 1 < len(raw_tokens) and \
                   (raw_tokens[i+1].replace('.', '', 1).isdigit() or raw_tokens[i+1] == '('):
                    processed_tokens.append('_UNARY_MINUS')
                else:
                    logging.error(f"Invalid expression: Unary minus must be followed by a number or an opening parenthesis. Token: {token}, Index: {i}")
                    raise ValueError("Invalid expression: Unary minus must be followed by a number or an opening parenthesis.")
            else:
                processed_tokens.append(token)
            i += 1
        logging.debug(f"Processed tokens (unary minus handled): {processed_tokens}")

        output_queue = []
        operator_stack = []

        for token in processed_tokens:
            if token.replace('.', '', 1).isdigit():  # It's a number (integer or float)
                output_queue.append(float(token))
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    logging.error("Mismatched parentheses: No matching opening parenthesis.")
                    raise ValueError("Mismatched parentheses.")
                operator_stack.pop()  # Pop the '('
            elif token in self.operators:  # It's an operator
                while (operator_stack and
                       operator_stack[-1] in self.operators and
                       ((self.operators[token]['associativity'] == 'left' and
                         self.operators[token]['precedence'] <= self.operators[operator_stack[-1]]['precedence']) or
                        (self.operators[token]['associativity'] == 'right' and
                         self.operators[token]['precedence'] < self.operators[operator_stack[-1]]['precedence']))):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            else:
                logging.error(f"Invalid token encountered: {token}")
                raise ValueError(f"Invalid token in expression: {token}")

        while operator_stack:
            op = operator_stack.pop()
            if op == '(':
                logging.error("Mismatched parentheses: Unclosed opening parenthesis.")
                raise ValueError("Mismatched parentheses.")
            output_queue.append(op)

        logging.debug(f"RPN (Output Queue): {output_queue}")

        # Evaluate RPN
        evaluation_stack = []
        for token in output_queue:
            if isinstance(token, float):
                evaluation_stack.append(token)
            elif token in self.operators:
                if token == '_UNARY_MINUS':
                    if len(evaluation_stack) < 1:
                        logging.error("Syntax error: Not enough operands for unary minus.")
                        raise ValueError("Syntax error: Not enough operands for unary minus.")
                    operand = evaluation_stack.pop()
                    result = self._apply_operator(token, operand)
                    evaluation_stack.append(result)
                else: # Binary operator
                    if len(evaluation_stack) < 2:
                        logging.error(f"Syntax error: Not enough operands for operator {token}.")
                        raise ValueError(f"Syntax error: Not enough operands for operator {token}.")
                    operand2 = evaluation_stack.pop()
                    operand1 = evaluation_stack.pop()
                    result = self._apply_operator(token, operand1, operand2)
                    evaluation_stack.append(result)
            else:
                logging.error(f"Unexpected token in RPN evaluation: {token}")
                raise ValueError(f"Unexpected token during RPN evaluation: {token}")

        if len(evaluation_stack) != 1:
            logging.error("Syntax error: Invalid expression format, final stack size not 1.")
            raise ValueError("Syntax error: Invalid expression format.")

        return evaluation_stack[0]
