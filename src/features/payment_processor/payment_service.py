import logging
from typing import Dict, Any

from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse
from src.utils.error_handling import handle_exceptions

logger = logging.getLogger(__name__)

class PaymentService:
    def __init__(self, payment_gateway: Any):
        self.payment_gateway = payment_gateway

    @handle_exceptions
    def process_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
        logger.info(f'Processing payment with gateway: {payment_request}')

        # Call payment gateway to process the payment
        gateway_response = self.payment_gateway.process_payment(payment_request.to_dict())

        # Create payment response
        payment_response = PaymentResponse(
            transaction_id=gateway_response['transaction_id'],
            status=gateway_response['status'],
            amount=payment_request.amount,
            currency=payment_request.currency
        )

        logger.info(f'Payment processed successfully: {payment_response}')
        return payment_response
