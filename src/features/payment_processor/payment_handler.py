import logging
from typing import Dict, Optional

from src.features.payment_processor.payment_service import PaymentService
from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse
from src.utils.error_handling import handle_exceptions

logger = logging.getLogger(__name__)

class PaymentHandler:
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    @handle_exceptions
    def process_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
        logger.info(f'Processing payment request: {payment_request}')

        payment_response = self.payment_service.process_payment(payment_request)

        logger.info(f'Payment processed successfully: {payment_response}')
        return payment_response

    @handle_exceptions
    def refund_payment(self, payment_id: str) -> Optional[PaymentResponse]:
        logger.info(f'Initiating refund for payment: {payment_id}')

        payment_response = self.payment_service.refund_payment(payment_id)

        if payment_response:
            logger.info(f'Payment refunded successfully: {payment_response}')
        else:
            logger.warning(f'Failed to refund payment: {payment_id}')

        return payment_response
