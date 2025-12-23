# Payment Processor

## Overview
The Payment Processor module is responsible for handling payment processing and refund operations. It provides a high-level interface for processing payments and initiating refunds, abstracting away the details of the underlying payment gateway.

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
    ├── error_handling.py
    └── payment_gateway.py

tests/
└── features/
    └── payment_processor/
        ├── test_payment_handler.py
        └── test_payment_service.py
```

## Test Case Structure
The tests for the Payment Processor module are organized into two test files:

1. `test_payment_handler.py`: Contains tests for the `PaymentHandler` class, which is responsible for processing payments and initiating refunds.
2. `test_payment_service.py`: Contains tests for the `PaymentService` class, which is responsible for interacting with the underlying payment gateway.

To run the tests, use the following command:

```
python -m unittest discover -s tests -p 'test_*.py'
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
2. Create an instance of the `PaymentService` class, passing in an instance of the `PaymentGateway` class:
   ```python
   payment_gateway = PaymentGateway()
   payment_service = PaymentService(payment_gateway)
   ```
3. Create an instance of the `PaymentHandler` class, passing in the `PaymentService` instance:
   ```python
   payment_handler = PaymentHandler(payment_service)
   ```
4. Use the `process_payment` method to process a payment:
   ```python
   payment_request = PaymentRequest(
       customer_id='customer123',
       amount=100.0,
       currency='USD',
       payment_method='credit_card'
   )
   payment_response = payment_handler.process_payment(payment_request)
   ```
5. Use the `refund_payment` method to initiate a refund:
   ```python
   refund_result = payment_handler.refund_payment('12345')
   ```

## Dependencies
The Payment Processor module has the following dependencies:

- Python 3.7+
- No external libraries

## Setup Instructions
1. Ensure you have Python 3.7 or higher installed on your system.
2. Clone the repository and navigate to the project directory.
3. The Payment Processor module is part of the main codebase and does not require any additional setup.

## API Documentation
The Payment Processor module provides the following API:

### `PaymentHandler`
- `process_payment(payment_request: PaymentRequest) -> PaymentResponse`: Processes a payment request and returns the payment response.
- `refund_payment(payment_id: str) -> Dict[str, Any]`: Initiates a refund for the specified payment and returns the refund result.

### `PaymentService`
- `process_payment(payment_request: PaymentRequest) -> PaymentResponse`: Sends the payment request to the underlying payment gateway and returns the payment response.
- `refund_payment(payment_id: str) -> Dict[str, Any]`: Sends the refund request to the underlying payment gateway and returns the refund result.

## Architecture
The Payment Processor module follows a layered architecture, with the following components:

1. `PaymentHandler`: This class is responsible for processing payments and initiating refunds. It acts as the main entry point for the module and handles error handling and logging.
2. `PaymentService`: This class is responsible for interacting with the underlying payment gateway. It encapsulates the details of the payment processing and refund operations.
3. `PaymentGateway`: This class is responsible for communicating with the external payment gateway. It abstracts away the details of the payment gateway API.
4. `PaymentRequest` and `PaymentResponse`: These data models represent the input and output of the payment processing and refund operations.
5. `ErrorHandling`: This utility module provides a decorator for handling exceptions and logging errors.

The layered architecture allows for better separation of concerns, testability, and maintainability of the codebase.
