import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def process_payment(payment_data: Dict[str, Any]) -> bool:
    """
    Process a payment using the payment processor.

    Args:
        payment_data (Dict[str, Any]): A dictionary containing payment details, such as amount, currency, and customer information.

    Returns:
        bool: True if the payment was processed successfully, False otherwise.
    """
    try:
        logger.info(f'Processing payment: {payment_data}')
        # Implement payment processing logic here
        # Call external payment gateway, update database, etc.
        return True
    except Exception as e:
        logger.error(f'Error processing payment: {e}', exc_info=True)
        return False
