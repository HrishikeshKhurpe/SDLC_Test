import unittest
from unittest.mock import patch, MagicMock

from src.features.payment_processor.payment_handler import PaymentHandler
from src.features.payment_processor.payment_service import PaymentService
from src.models.payment_request import PaymentRequest
from src.models.payment_response import PaymentResponse
from src.utils.error_handling import PaymentProcessingError

class TestPaymentHandler(unittest.TestCase):
    def setUp(self):
        self.payment_service = MagicMock(spec=PaymentService)
        self.payment_handler = PaymentHandler(self.payment_service)

    @patch('src.features.payment_processor.payment_handler.logger')
    def test_process_payment_success(self, mock_logger):
        payment_request = PaymentRequest(
            customer_id='customer123',
            amount=100.0,
            payment_method='credit_card',
            currency='USD',
            description='Test payment'
        )
        payment_response = PaymentResponse(
            transaction_id='tx123',
            status='success',
            amount=100.0,
            currency='USD',
            payment_method='credit_card',
            customer_id='customer123',
            description='Test payment'
        )
        self.payment_service.process_payment.return_value = payment_response

        result = self.payment_handler.process_payment(payment_request)

        self.assertEqual(result, payment_response)
        self.payment_service.process_payment.assert_called_once_with(payment_request)
        mock_logger.info.assert_any_call(f'Processing payment request: {payment_request}')
        mock_logger.info.assert_any_call(f'Payment processing completed: {payment_response}')

    @patch('src.features.payment_processor.payment_handler.logger')
    def test_process_payment_failure(self, mock_logger):
        payment_request = PaymentRequest(
            customer_id='customer123',
            amount=100.0,
            payment_method='credit_card',
            currency='USD',
            description='Test payment'
        )
        self.payment_service.process_payment.side_effect = PaymentProcessingError('Payment failed')

        with self.assertRaises(PaymentProcessingError):
            self.payment_handler.process_payment(payment_request)

        self.payment_service.process_payment.assert_called_once_with(payment_request)
        mock_logger.info.assert_called_once_with(f'Processing payment request: {payment_request}')
        mock_logger.error.assert_called_once()
