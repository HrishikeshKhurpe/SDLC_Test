from flask import Blueprint, request, jsonify, current_app
from src.calculator.service import calculate

calculator_bp = Blueprint('calculator_bp', __name__)

@calculator_bp.route('/calculate', methods=['POST'])
def handle_calculate():
    """
    Handles calculation requests.
    Expects a JSON payload with 'operand1', 'operand2', and 'operation'.
    """
    try:
        data = request.get_json()
        if not data:
            current_app.logger.warning("Received empty or invalid JSON payload.")
            return jsonify({"error": "Invalid JSON payload"}), 400

        current_app.logger.info(f"Received calculation request: {data}")

        operand1 = data.get('operand1')
        operand2 = data.get('operand2')
        operation = data.get('operation')

        if operand1 is None or operand2 is None or operation is None:
            missing_params = []
            if operand1 is None: missing_params.append("operand1")
            if operand2 is None: missing_params.append("operand2")
            if operation is None: missing_params.append("operation")
            error_msg = f"Missing required parameters: {', '.join(missing_params)}"
            current_app.logger.warning(f"Bad request: {error_msg}")
            return jsonify({"error": error_msg}), 400

        if not isinstance(operand1, (int, float)) or not isinstance(operand2, (int, float)):
            error_msg = "Operands must be numeric"
            current_app.logger.warning(f"Bad request: {error_msg}. Received operand1: {operand1}, operand2: {operand2}")
            return jsonify({"error": error_msg}), 400

        result = calculate(operand1, operand2, operation)
        
        response = {"result": result}
        current_app.logger.info(f"Calculation successful: {operand1} {operation} {operand2} = {result}")
        return jsonify(response), 200

    except ValueError as ve:
        current_app.logger.warning(f"Value error during calculation: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        # Log the full exception for unexpected errors
        current_app.logger.error("An unexpected error occurred during calculation", exc_info=True)
        return jsonify({"error": "An unexpected internal error occurred"}), 500
