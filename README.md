# Payment Processor

## Overview
The Payment Processor module is responsible for handling payment processing functionality for the application. It provides an abstraction over a payment gateway and exposes a simple interface for processing payments.

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

To run the tests, use the following command:

```
pytest tests/features/payment_processor/
```

## Run Book
To use the Payment Processor module, follow these steps:

1. Ensure you have the required dependencies installed (see the Dependencies section below).
2. Import the necessary classes and models:
   ```python
   from src.features.payment_processor.payment_handler import PaymentHandler
   from src.features.payment_processor.payment_service import PaymentService
   from src.models.payment_request import PaymentRequest
   ```
3. Create an instance of the `PaymentService` and `PaymentHandler`:
   ```python
   payment_service = PaymentService(payment_gateway=payment_gateway)
   payment_handler = PaymentHandler(payment_service=payment_service)
   ```
4. Create a `PaymentRequest` and pass it to the `process_payment` method of the `PaymentHandler`:
   ```python
   payment_request = PaymentRequest(
       customer_id='customer123',
       amount=100.0,
       payment_method='credit_card'
   )
   payment_response = payment_handler.process_payment(payment_request)
   ```
5. The `PaymentResponse` object will contain the details of the processed payment.

## Dependencies
- `python>=3.7`
- `dataclasses` (part of Python standard library since 3.7)

## Setup Instructions
1. Create a new Python virtual environment.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Ensure all tests pass:
   ```
   pytest tests/
   ```
4. You're now ready to use the Payment Processor module in your application.

## API Documentation
The main classes and their methods are:

1. `PaymentHandler`:
   - `process_payment(payment_request: PaymentRequest) -> PaymentResponse`

2. `PaymentService`:
   - `process_payment(payment_request: PaymentRequest) -> PaymentResponse`

3. `PaymentRequest`:
   - `to_dict() -> Dict[str, Any]`
   - `from_dict(data: Dict[str, Any]) -> PaymentRequest`

4. `PaymentResponse`:
   - `from_dict(data: Dict[str, Any]) -> PaymentResponse`

## Architecture
The Payment Processor module consists of the following components:

1. `PaymentHandler`: This is the main entry point for processing payments. It takes a `PaymentRequest` object and delegates the actual payment processing to the `PaymentService`.

2. `PaymentService`: This class encapsulates the logic for interacting with the payment gateway. It handles the payment processing and returns a `PaymentResponse` object.

3. `PaymentRequest` and `PaymentResponse`: These are data models that represent the input and output of the payment processing.

4. `error_handling.py`: This module contains the custom exception class `PaymentProcessingError` and a decorator `handle_exceptions` that wraps functions to handle unexpected exceptions.
