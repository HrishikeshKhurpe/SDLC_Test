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
            logger.error(f'Unexpected error occurred: {e}', exc_info=True)
            raise e
    return wrapper
