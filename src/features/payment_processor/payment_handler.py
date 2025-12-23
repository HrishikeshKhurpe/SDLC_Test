import logging
from typing import Dict, Any

from src.features.payment_processor.payment_service import process_payment

logger = logging.getLogger(__name__)

def handle_payment(payment_data: Dict[str, Any]) -> bool:
    """
    Handle a payment request.

    Args:
        payment_data (Dict[str, Any]): A dictionary containing payment details, such as amount, currency, and customer information.

    Returns:
        bool: True if the payment was processed successfully, False otherwise.
    """
    try:
        logger.info(f'Received payment request: {payment_data}')
        success = process_payment(payment_data)
        if success:
            logger.info('Payment processed successfully')
        else:
            logger.error('Payment processing failed')
        return success
    except Exception as e:
        logger.error(f'Error processing payment: {e}', exc_info=True)
        return False
