import logging
from functools import wraps
from typing import Callable

logger = logging.getLogger(__name__)

class PaymentProcessingError(Exception):
    pass

def handle_exceptions(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Error occurred in {func.__name__}: {str(e)}', exc_info=True)
            if isinstance(e, PaymentProcessingError):
                raise e
            else:
                raise PaymentProcessingError(f'An error occurred while processing the payment: {str(e)}') from e
    return wrapper
