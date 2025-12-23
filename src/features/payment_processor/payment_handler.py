import logging
from typing import Dict, Any
from src.features.payment_processor.payment_service import PaymentService
from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse
from src.utils.error_handling import handle_exceptions

class PaymentHandler:
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    @handle_exceptions
    def process_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
        logging.info(f'Processing payment request: {payment_request}')
        payment_response = self.payment_service.process_payment(payment_request)
        logging.info(f'Payment processing completed: {payment_response}')
        return payment_response

    @handle_exceptions
    def refund_payment(self, payment_id: str) -> Dict[str, Any]:
        logging.info(f'Initiating refund for payment: {payment_id}')
        refund_result = self.payment_service.refund_payment(payment_id)
        logging.info(f'Refund completed: {refund_result}')
        return refund_result
