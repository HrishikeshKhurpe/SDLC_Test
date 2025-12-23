# Payment Processor

## Overview
The Payment Processor module is responsible for handling payment requests and processing payments using an external payment gateway.

## File Structure
```
src/
├── features/
│   └── payment_processor/
│       ├── payment_handler.py
│       └── payment_service.py
└── tests/
    └── features/
        └── payment_processor/
            └── test_payment_handler.py
```

## Test Case Structure
The tests for the Payment Processor module are located in the `src/tests/features/payment_processor` directory. The test cases cover the following scenarios:

1. `test_handle_payment_success`: Verifies that the `handle_payment` function correctly processes a successful payment.
2. `test_handle_payment_failure`: Verifies that the `handle_payment` function correctly handles a failed payment.
3. `test_handle_payment_exception`: Verifies that the `handle_payment` function correctly handles exceptions during payment processing.

To run the tests, use the following command:

```
python -m unittest discover -s src/tests -p 'test_*.py'
```

## Run Book
To use the Payment Processor module, follow these steps:

1. Ensure that all required dependencies are installed (see the Dependencies section below).
2. Import the `handle_payment` function from the `src.features.payment_processor.payment_handler` module.
3. Call the `handle_payment` function with a dictionary of payment data, such as:

```python
payment_data = {
    'amount': 100,
    'currency': 'USD',
    'customer': {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
}
success = handle_payment(payment_data)
if success:
    print('Payment processed successfully')
else:
    print('Payment processing failed')
```

## Dependencies
The Payment Processor module has the following dependencies:

- Python 3.7 or higher
- No external libraries

## Setup Instructions
1. Ensure that you have Python 3.7 or higher installed on your system.
2. Clone the repository and navigate to the project directory.
3. (Optional) Create a virtual environment and activate it.
4. Install the required dependencies (if any) using the following command:

```
pip install -r requirements.txt
```

## API Documentation
The Payment Processor module provides the following API:

1. `handle_payment(payment_data: Dict[str, Any]) -> bool`:
   - Handles a payment request by processing the payment using the `process_payment` function.
   - `payment_data` is a dictionary containing payment details, such as amount, currency, and customer information.
   - Returns `True` if the payment was processed successfully, `False` otherwise.

2. `process_payment(payment_data: Dict[str, Any]) -> bool`:
   - Processes a payment using the payment processor.
   - `payment_data` is a dictionary containing payment details, such as amount, currency, and customer information.
   - Returns `True` if the payment was processed successfully, `False` otherwise.

## Architecture
The Payment Processor module consists of two main components:

1. `payment_handler.py`: This module is responsible for handling payment requests and delegating the actual payment processing to the `payment_service.py` module.
2. `payment_service.py`: This module is responsible for processing payments using the external payment gateway. It contains the core payment processing logic.

The `payment_handler.py` module acts as a facade, providing a simple interface for handling payment requests, while the `payment_service.py` module encapsulates the payment processing logic. This separation of concerns ensures that the payment handling and processing logic are decoupled, making the code more maintainable and testable.
