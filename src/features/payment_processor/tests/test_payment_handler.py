import unittest
from unittest.mock import patch
from src.features.payment_processor.payment_handler import handle_payment

class TestPaymentHandler(unittest.TestCase):
    @patch('src.features.payment_processor.payment_handler.process_payment')
    def test_handle_payment_success(self, mock_process_payment):
        mock_process_payment.return_value = True
        payment_data = {
            'amount': 100.0,
            'currency': 'USD',
            'customer': {
                'name': 'John Doe',
                'email': 'john.doe@example.com'
            }
        }
        result = handle_payment(payment_data)
        self.assertTrue(result)

    @patch('src.features.payment_processor.payment_handler.process_payment')
    def test_handle_payment_failure(self, mock_process_payment):
        mock_process_payment.return_value = False
        payment_data = {
            'amount': 100.0,
            'currency': 'USD',
            'customer': {
                'name': 'John Doe',
                'email': 'john.doe@example.com'
            }
        }
        result = handle_payment(payment_data)
        self.assertFalse(result)

    @patch('src.features.payment_processor.payment_handler.process_payment')
    def test_handle_payment_exception(self, mock_process_payment):
        mock_process_payment.side_effect = Exception('Payment processing error')
        payment_data = {
            'amount': 100.0,
            'currency': 'USD',
            'customer': {
                'name': 'John Doe',
                'email': 'john.doe@example.com'
            }
        }
        result = handle_payment(payment_data)
        self.assertFalse(result)
