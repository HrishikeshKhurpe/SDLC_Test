import logging
from typing import Dict, Any

from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse
from src.utils.error_handling import handle_exceptions, PaymentProcessingError

logger = logging.getLogger(__name__)

class PaymentService:
    def __init__(self, payment_gateway: Any):
        self.payment_gateway = payment_gateway

    @handle_exceptions
    def process_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
        logger.info(f'Initiating payment processing for request: {payment_request}')

        try:
            payment_response = self.payment_gateway.make_payment(payment_request.to_dict())
            logger.info(f'Payment processing successful: {payment_response}')
            return PaymentResponse.from_dict(payment_response)
        except Exception as e:
            logger.error(f'Error processing payment: {e}', exc_info=True)
            raise PaymentProcessingError('Failed to process payment') from e
