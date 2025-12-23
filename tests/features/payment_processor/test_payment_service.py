import unittest
from unittest.mock import patch, MagicMock

from src.features.payment_processor.payment_service import PaymentService
from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse
from src.utils.error_handling import PaymentProcessingError

class TestPaymentService(unittest.TestCase):
    def setUp(self):
        self.payment_gateway = MagicMock()
        self.payment_service = PaymentService(self.payment_gateway)

    @patch('src.features.payment_processor.payment_service.logger')
    def test_process_payment_success(self, mock_logger):
        payment_request = PaymentRequest(
            customer_id='customer123',
            amount=100.0,
            payment_method='credit_card',
            currency='USD',
            description='Test payment'
        )
        payment_response_data = {
            'transaction_id': 'tx123',
            'status': 'success',
            'amount': 100.0,
            'currency': 'USD',
            'payment_method': 'credit_card',
            'customer_id': 'customer123',
            'description': 'Test payment'
        }
        self.payment_gateway.process_payment.return_value = payment_response_data

        result = self.payment_service.process_payment(payment_request)

        self.assertEqual(result, PaymentResponse(**payment_response_data))
        self.payment_gateway.process_payment.assert_called_once_with(payment_request.to_dict())
        mock_logger.info.assert_any_call(f'Initiating payment processing for request: {payment_request}')

    @patch('src.features.payment_processor.payment_service.logger')
    def test_process_payment_failure(self, mock_logger):
        payment_request = PaymentRequest(
            customer_id='customer123',
            amount=100.0,
            payment_method='credit_card',
            currency='USD',
            description='Test payment'
        )
        self.payment_gateway.process_payment.side_effect = Exception('Payment failed')

        with self.assertRaises(PaymentProcessingError):
            self.payment_service.process_payment(payment_request)

        self.payment_gateway.process_payment.assert_called_once_with(payment_request.to_dict())
        mock_logger.info.assert_called_once_with(f'Initiating payment processing for request: {payment_request}')
        mock_logger.error.assert_called_once()
