# Payment Processor

## Overview
The Payment Processor module is responsible for handling payment processing and refund operations. It provides a `PaymentHandler` class that acts as the entry point for processing payments and refunds, and a `PaymentService` class that encapsulates the logic for interacting with the payment gateway.

## File Structure
```
src/
├── features/
│   └── payment_processor/
│       ├── payment_handler.py
│       ├── payment_service.py
│       └── payment_gateway.py
├── models/
│   ├── payment_request.py
│   └── payment_response.py
└── utils/
    └── error_handling.py
```

## Test Case Structure
The test cases for the Payment Processor module are located in the `tests/features/payment_processor` directory. The test suite covers the following scenarios:

- Successful payment processing
- Failed payment processing
- Successful payment refund
- Failed payment refund
- Edge cases and error handling

To run the tests, execute the following command from the project root directory:

```
python -m unittest discover -s tests -p "*_test.py"
```

## Run Book
To use the Payment Processor module, follow these steps:

1. Instantiate a `PaymentGateway` object with the necessary API credentials.
2. Create a `PaymentService` object, passing the `PaymentGateway` instance.
3. Use the `PaymentHandler` class to process payments and refunds.

Example usage:

```python
from src.features.payment_processor.payment_handler import PaymentHandler
from src.features.payment_processor.payment_service import PaymentService
from src.features.payment_processor.payment_gateway import PaymentGateway
from src.models.payment_request import PaymentRequest

payment_gateway = PaymentGateway(api_key='your_api_key', api_secret='your_api_secret')
payment_service = PaymentService(payment_gateway)
payment_handler = PaymentHandler(payment_service)

payment_request = PaymentRequest(
    amount=100.00,
    currency='USD',
    card_number='4111111111111111',
    expiry_date='12/24',
    cvv='123',
    customer_name='John Doe'
)

payment_response = payment_handler.process_payment(payment_request)
if payment_response.success:
    print(f'Payment processed successfully. Transaction ID: {payment_response.transaction_id}')
else:
    print(f'Payment processing failed: {payment_response.error_message}')
```

## Dependencies
The Payment Processor module has the following dependencies:

- Python 3.7+
- No external libraries

## Setup Instructions
1. Ensure you have Python 3.7 or higher installed on your system.
2. Clone the repository and navigate to the project directory.
3. (Optional) Create a virtual environment and activate it.
4. Install the required dependencies (if any) using `pip install -r requirements.txt`.

## API Documentation
The Payment Processor module provides the following API:

### `PaymentHandler`
- `process_payment(payment_request: PaymentRequest) -> PaymentResponse`
- `refund_payment(payment_id: str) -> Optional[PaymentResponse]`

### `PaymentService`
- `process_payment(payment_request: PaymentRequest) -> PaymentResponse`
- `refund_payment(payment_id: str) -> Optional[PaymentResponse]`

### `PaymentGateway`
- `process_payment(payment_request: PaymentRequest) -> PaymentResponse`
- `refund_payment(payment_id: str) -> PaymentResponse`

## Architecture
The Payment Processor module follows a layered architecture:

1. `PaymentHandler`: The entry point for processing payments and refunds. It orchestrates the interaction between the `PaymentService` and the external payment gateway.
2. `PaymentService`: Encapsulates the business logic for processing payments and refunds. It handles communication with the `PaymentGateway`.
3. `PaymentGateway`: Responsible for interacting with the external payment gateway API. It abstracts the details of the payment gateway implementation.
4. `PaymentRequest` and `PaymentResponse`: Data models for representing payment-related information.
5. `error_handling.py`: Provides a decorator for handling exceptions and logging errors.

The module is designed to be extensible and testable, with clear separation of concerns and dependency management.
