import logging
from typing import Dict, Any
from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse
from src.utils.payment_gateway import PaymentGateway
from src.utils.error_handling import handle_exceptions

class PaymentService:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    @handle_exceptions
    def process_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
        logging.info(f'Sending payment request to gateway: {payment_request}')
        payment_response = self.payment_gateway.process_payment(payment_request)
        logging.info(f'Payment gateway response: {payment_response}')
        return payment_response

    @handle_exceptions
    def refund_payment(self, payment_id: str) -> Dict[str, Any]:
        logging.info(f'Sending refund request to gateway for payment: {payment_id}')
        refund_result = self.payment_gateway.refund_payment(payment_id)
        logging.info(f'Refund gateway response: {refund_result}')
        return refund_result
