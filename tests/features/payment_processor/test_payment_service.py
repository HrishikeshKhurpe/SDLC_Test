import unittest
from unittest.mock import patch
from src.features.payment_processor.payment_service import PaymentService
from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse
from src.utils.payment_gateway import PaymentGateway

class TestPaymentService(unittest.TestCase):
    @patch('src.utils.payment_gateway.PaymentGateway')
    def test_process_payment(self, mock_payment_gateway):
        mock_gateway = mock_payment_gateway.return_value
        mock_gateway.process_payment.return_value = PaymentResponse(payment_id='12345', status='SUCCESS', amount=100.0, currency='USD')

        payment_request = PaymentRequest(customer_id='customer123', amount=100.0, currency='USD', payment_method='credit_card')
        payment_service = PaymentService(mock_gateway)
        payment_response = payment_service.process_payment(payment_request)

        self.assertEqual(payment_response.payment_id, '12345')
        self.assertEqual(payment_response.status, 'SUCCESS')
        self.assertEqual(payment_response.amount, 100.0)
        self.assertEqual(payment_response.currency, 'USD')
        mock_gateway.process_payment.assert_called_with(payment_request)

    @patch('src.utils.payment_gateway.PaymentGateway')
    def test_refund_payment(self, mock_payment_gateway):
        mock_gateway = mock_payment_gateway.return_value
        mock_gateway.refund_payment.return_value = {'status': 'SUCCESS', 'amount': 50.0}

        payment_service = PaymentService(mock_gateway)
        refund_result = payment_service.refund_payment('12345')

        self.assertEqual(refund_result['status'], 'SUCCESS')
        self.assertEqual(refund_result['amount'], 50.0)
        mock_gateway.refund_payment.assert_called_with('12345')
