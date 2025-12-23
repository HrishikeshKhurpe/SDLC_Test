import logging
from typing import Dict, Any
from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse

class PaymentGateway:
    def process_payment(self, payment_request: PaymentRequest) -> PaymentResponse:
        logging.info(f'Sending payment to external gateway: {payment_request}')
        # Implement logic to send payment to external gateway and return response
        payment_id = '12345'
        status = 'SUCCESS'
        message = 'Payment processed successfully'
        return PaymentResponse(payment_id=payment_id, status=status, amount=payment_request.amount, currency=payment_request.currency, message=message)

    def refund_payment(self, payment_id: str) -> Dict[str, Any]:
        logging.info(f'Sending refund request to external gateway for payment: {payment_id}')
        # Implement logic to send refund request to external gateway and return response
        refund_status = 'SUCCESS'
        refund_amount = 50.0
        return {'status': refund_status, 'amount': refund_amount}
