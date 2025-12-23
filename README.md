# Payment Processor

## Overview
The Payment Processor module is responsible for handling payment requests and processing payments using an external payment gateway. It provides a `handle_payment` function that takes payment details as input and returns a boolean indicating whether the payment was processed successfully or not.

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
The test cases for the Payment Processor module are located in the `src/tests/features/payment_processor/test_payment_handler.py` file. The test suite covers the following scenarios:

1. `test_handle_payment_success`: Verifies that the `handle_payment` function returns `True` when the payment is processed successfully.
2. `test_handle_payment_failure`: Verifies that the `handle_payment` function returns `False` when the payment processing fails.
3. `test_handle_payment_exception`: Verifies that the `handle_payment` function returns `False` when an exception is raised during payment processing.

To run the tests, use the following command:

```
python -m unittest discover -s src/tests -p 'test_*.py'
```

## Run Book
To use the Payment Processor module, follow these steps:

1. Import the `handle_payment` function from the `src.features.payment_processor.payment_handler` module.
2. Prepare a dictionary containing the payment details, such as `amount`, `currency`, and `customer` information.
3. Call the `handle_payment` function with the payment data as an argument.
4. The function will return `True` if the payment was processed successfully, and `False` otherwise.

Example usage:

```python
from src.features.payment_processor.payment_handler import handle_payment

payment_data = {
    'amount': 100.0,
    'currency': 'USD',
    'customer': {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
}

if handle_payment(payment_data):
    print('Payment processed successfully')
else:
    print('Payment processing failed')
```

## Dependencies
The Payment Processor module has the following dependencies:

- Python 3.7 or higher
- No external libraries

## Setup Instructions
1. Ensure you have Python 3.7 or higher installed on your system.
2. Clone the repository and navigate to the project directory.
3. The Payment Processor module is part of the main codebase and does not require any additional setup.

## API Documentation
The Payment Processor module provides the following API:

### `handle_payment(payment_data: Dict[str, Any]) -> bool`
Handles a payment request.

**Args:**
- `payment_data (Dict[str, Any])`: A dictionary containing payment details, such as amount, currency, and customer information.

**Returns:**
- `bool`: `True` if the payment was processed successfully, `False` otherwise.

## Architecture
The Payment Processor module consists of two main components:

1. `payment_handler.py`: This module is responsible for handling the payment request, logging the process, and calling the `payment_service.py` module to process the payment.
2. `payment_service.py`: This module contains the logic for processing the payment, such as calling the external payment gateway, updating the database, and handling any exceptions that may occur during the process.

The `payment_handler.py` module acts as the entry point for the payment processing functionality, while the `payment_service.py` module encapsulates the core payment processing logic.
