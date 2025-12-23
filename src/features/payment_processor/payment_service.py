import logging
from typing import Dict, Optional

from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse
from src.utils.error_handling import handle_exceptions, PaymentProcessingError

logger = logging.getLogger(__name__)

class PaymentService:
    def __init__(self, payment_gateway: 'PaymentGateway'):
        self.payment_gateway = payment_gateway

    @handle_exceptions
    def process_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
        logger.info(f'Initiating payment processing: {payment_request}')

        payment_response = self.payment_gateway.process_payment(payment_request)

        if payment_response.success:
            logger.info(f'Payment processed successfully: {payment_response}')
        else:
            logger.error(f'Payment processing failed: {payment_response}')
            raise PaymentProcessingError(payment_response.error_message)

        return payment_response

    @handle_exceptions
    def refund_payment(self, payment_id: str) -> Optional[PaymentResponse]:
        logger.info(f'Initiating refund for payment: {payment_id}')

        payment_response = self.payment_gateway.refund_payment(payment_id)

        if payment_response.success:
            logger.info(f'Payment refunded successfully: {payment_response}')
        else:
            logger.error(f'Failed to refund payment: {payment_id}')

        return payment_response
