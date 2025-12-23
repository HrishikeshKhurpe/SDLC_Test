# Payment Processor

## Overview
The Payment Processor module provides functionality to process payments using a payment gateway. It includes a `PaymentHandler` that orchestrates the payment processing flow and a `PaymentService` that interacts with the payment gateway.

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
tests/
├── features/
│   └── payment_processor/
│       ├── test_payment_handler.py
│       └── test_payment_service.py
```

## Test Case Structure
The tests for the Payment Processor module are organized in the `tests/features/payment_processor` directory. The test cases cover the following scenarios:

- `test_payment_handler_success`: Verifies the successful processing of a payment request.
- `test_payment_handler_failure`: Verifies the handling of a payment processing failure.
- `test_payment_service_success`: Verifies the successful processing of a payment request by the `PaymentService`.
- `test_payment_service_failure`: Verifies the handling of a payment processing failure by the `PaymentService`.

To run the tests, use the following command:

```
python -m unittest discover -s tests -p 'test_*.py'
```

## Run Book
To use the Payment Processor module, follow these steps:

1. Create a `PaymentRequest` object with the necessary details:

   ```python
   from src.models.payment_request import PaymentRequest

   payment_request = PaymentRequest(
       customer_id='customer123',
       amount=100.0,
       payment_method='credit_card',
       currency='USD',
       description='Test payment'
   )
   ```

2. Create a `PaymentService` instance and pass it to the `PaymentHandler`:

   ```python
   from src.features.payment_processor.payment_service import PaymentService
   from src.features.payment_processor.payment_handler import PaymentHandler

   payment_gateway = # Initialize payment gateway
   payment_service = PaymentService(payment_gateway)
   payment_handler = PaymentHandler(payment_service)
   ```

3. Call the `process_payment` method on the `PaymentHandler` to process the payment:

   ```python
   payment_response = payment_handler.process_payment(payment_request)
   print(payment_response)
   ```

## Dependencies
The Payment Processor module requires the following dependencies:

- `dataclasses` (built-in)
- `typing` (built-in)
- `logging` (built-in)
- `functools` (built-in)

## Setup Instructions
1. Ensure you have Python 3.7 or higher installed.
2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Configure the payment gateway integration by providing the necessary credentials or settings.

## API Documentation
The Payment Processor module provides the following API:

### `PaymentRequest`
- `customer_id: str`
- `amount: float`
- `payment_method: str`
- `currency: str = 'USD'`
- `description: Optional[str] = None`
- `to_dict() -> dict`

### `PaymentResponse`
- `transaction_id: str`
- `status: str`
- `amount: float`
- `currency: str`
- `payment_method: str`
- `customer_id: str`
- `description: Optional[str] = None`

### `PaymentHandler`
- `process_payment(payment_request: PaymentRequest) -> PaymentResponse`

### `PaymentService`
- `process_payment(payment_request: PaymentRequest) -> PaymentResponse`

## Architecture
The Payment Processor module follows a layered architecture:

1. **Payment Handler**: The `PaymentHandler` class is responsible for orchestrating the payment processing flow. It receives a `PaymentRequest`, passes it to the `PaymentService`, and returns the `PaymentResponse`.

2. **Payment Service**: The `PaymentService` class is responsible for interacting with the payment gateway. It receives a `PaymentRequest`, calls the payment gateway, and returns a `PaymentResponse`.

3. **Models**: The `PaymentRequest` and `PaymentResponse` models define the data structures used throughout the module.

4. **Error Handling**: The `error_handling` module provides a custom exception (`PaymentProcessingError`) and a decorator (`handle_exceptions`) to handle exceptions and log errors.

The module is designed to be extensible and testable. The `PaymentService` can be easily swapped out with a different implementation, and the `PaymentHandler` can be tested in isolation from the `PaymentService`.
