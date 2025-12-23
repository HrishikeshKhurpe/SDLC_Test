import logging
from typing import Dict, Any

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

        logger.info(f'Payment processing completed: {payment_response}')
        return payment_response
