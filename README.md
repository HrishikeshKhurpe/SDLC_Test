# Payment Processor

## Overview
The Payment Processor module is responsible for handling payment processing functionality for the application. It provides an abstraction over a payment gateway and exposes a simple API for processing payments.

## File Structure
```
src/
├── features/
│   └── payment_processor/
│       ├── payment_handler.py
│       └── payment_service.py
├── models/
│   ├── payment_request.py
│   └── payment_response.py
└── utils/
    └── error_handling.py
```

## Test Case Structure
The test cases for the Payment Processor module are organized as follows:

- `tests/features/payment_processor/test_payment_handler.py`
- `tests/features/payment_processor/test_payment_service.py`
- `tests/models/test_payment_request.py`
- `tests/models/test_payment_response.py`
- `tests/utils/test_error_handling.py`

To run the tests, use the following command:

```
python -m unittest discover tests
```

## Run Book
To use the Payment Processor module, follow these steps:

1. Import the necessary classes and models:
   ```python
   from src.features.payment_processor.payment_handler import PaymentHandler
   from src.features.payment_processor.payment_service import PaymentService
   from src.models.payment_request import PaymentRequest
   from src.models.payment_response import PaymentResponse
   ```

2. Create an instance of the `PaymentService` and `PaymentHandler`:
   ```python
   payment_service = PaymentService(payment_gateway=some_payment_gateway_instance)
   payment_handler = PaymentHandler(payment_service=payment_service)
   ```

3. Create a `PaymentRequest` and pass it to the `PaymentHandler.process_payment()` method:
   ```python
   payment_request = PaymentRequest(
       customer_id='customer123',
       amount=100.0,
       payment_method='credit_card'
   )
   payment_response = payment_handler.process_payment(payment_request)
   ```

4. The `PaymentResponse` object will contain the details of the processed payment.

## Dependencies
- Python 3.9+
- No external dependencies

## Setup Instructions
1. Ensure you have Python 3.9 or higher installed.
2. Create a new virtual environment and activate it.
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. You're now ready to use the Payment Processor module.

## API Documentation
The Payment Processor module provides the following API:

### `PaymentHandler`
- `process_payment(payment_request: PaymentRequest) -> PaymentResponse`
  - Processes a payment request and returns a payment response.

### `PaymentService`
- `process_payment(payment_request: PaymentRequest) -> PaymentResponse`
  - Processes a payment request using the configured payment gateway and returns a payment response.

### `PaymentRequest`
- `customer_id: str`
- `amount: float`
- `payment_method: str`
- `to_dict() -> Dict[str, Any]`
  - Converts the `PaymentRequest` object to a dictionary.
- `from_dict(data: Dict[str, Any]) -> PaymentRequest`
  - Creates a `PaymentRequest` object from a dictionary.

### `PaymentResponse`
- `transaction_id: str`
- `status: str`
- `amount: float`
- `payment_method: str`
- `from_dict(data: Dict[str, Any]) -> PaymentResponse`
  - Creates a `PaymentResponse` object from a dictionary.

## Architecture
The Payment Processor module follows a layered architecture:

1. **Payment Handler**: Provides a high-level API for processing payments. Handles error handling and logging.
2. **Payment Service**: Encapsulates the logic for interacting with the payment gateway. Responsible for making the actual payment processing calls.
3. **Models**: Defines the data structures for payment requests and responses.
4. **Utilities**: Provides utility functions, such as the `handle_exceptions` decorator for error handling.

The `PaymentHandler` class is the main entry point for the module, and it delegates the actual payment processing to the `PaymentService` class. The `PaymentService` class interacts with the payment gateway to process the payment. The `PaymentRequest` and `PaymentResponse` models are used to represent the input and output of the payment processing.

The `handle_exceptions` decorator in the `error_handling` module is used to provide consistent error handling across the module.
