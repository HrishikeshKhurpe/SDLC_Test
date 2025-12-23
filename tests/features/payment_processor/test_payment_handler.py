import unittest
from unittest.mock import patch
from src.features.payment_processor.payment_handler import PaymentHandler
from src.features.payment_processor.payment_service import PaymentService
from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse

class TestPaymentHandler(unittest.TestCase):
    @patch('src.features.payment_processor.payment_service.PaymentService')
    def test_process_payment(self, mock_payment_service):
        mock_service = mock_payment_service.return_value
        mock_service.process_payment.return_value = PaymentResponse(payment_id='12345', status='SUCCESS', amount=100.0, currency='USD')

        payment_request = PaymentRequest(customer_id='customer123', amount=100.0, currency='USD', payment_method='credit_card')
        payment_handler = PaymentHandler(mock_service)
        payment_response = payment_handler.process_payment(payment_request)

        self.assertEqual(payment_response.payment_id, '12345')
        self.assertEqual(payment_response.status, 'SUCCESS')
        self.assertEqual(payment_response.amount, 100.0)
        self.assertEqual(payment_response.currency, 'USD')
        mock_service.process_payment.assert_called_with(payment_request)

    @patch('src.features.payment_processor.payment_service.PaymentService')
    def test_refund_payment(self, mock_payment_service):
        mock_service = mock_payment_service.return_value
        mock_service.refund_payment.return_value = {'status': 'SUCCESS', 'amount': 50.0}

        payment_handler = PaymentHandler(mock_service)
        refund_result = payment_handler.refund_payment('12345')

        self.assertEqual(refund_result['status'], 'SUCCESS')
        self.assertEqual(refund_result['amount'], 50.0)
        mock_service.refund_payment.assert_called_with('12345')
