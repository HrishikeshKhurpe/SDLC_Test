# Payment Processor

## Overview
The Payment Processor module is responsible for processing payments for the application. It provides a `PaymentHandler` that interacts with a `PaymentService` to process payment requests and generate payment responses.

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
The test cases for the Payment Processor module are located in the `tests/features/payment_processor` directory. The test suite covers the following scenarios:

- Successful payment processing
- Invalid payment request
- Error handling in the `PaymentHandler` and `PaymentService`

To run the tests, use the following command:

```
pytest tests/features/payment_processor
```

## Run Book
To use the Payment Processor module, follow these steps:

1. Create a `PaymentRequest` object with the necessary details:

```python
from src.models.payment_request import PaymentRequest

payment_request = PaymentRequest(
    user_id='user123',
    amount=100.0,
    currency='USD',
    payment_method='credit_card',
    card_number='4111111111111111',
    expiry_date='12/24',
    cvv='123'
)
```

2. Create a `PaymentService` instance and a `PaymentHandler` instance:

```python
from src.features.payment_processor.payment_service import PaymentService
from src.features.payment_processor.payment_handler import PaymentHandler

payment_service = PaymentService(payment_gateway=some_payment_gateway)
payment_handler = PaymentHandler(payment_service=payment_service)
```

3. Call the `process_payment` method on the `PaymentHandler` to process the payment:

```python
payment_response = payment_handler.process_payment(payment_request)
print(payment_response)
```

## Dependencies
- Python 3.9+
- `dataclasses` (built-in)
- `typing` (built-in)
- `logging` (built-in)

## Setup Instructions
1. Ensure you have Python 3.9 or higher installed.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Configure the payment gateway integration in the `PaymentService` class.

## Architecture
The Payment Processor module follows a service-oriented architecture. The `PaymentHandler` class is responsible for validating the input, calling the `PaymentService` to process the payment, and returning the `PaymentResponse`. The `PaymentService` class is responsible for interacting with the payment gateway to process the payment.

The `PaymentRequest` and `PaymentResponse` models encapsulate the data required for payment processing and the response, respectively. The `error_handling` utility module provides a decorator to handle exceptions and log errors.
