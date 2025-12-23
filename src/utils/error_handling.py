import logging
from functools import wraps

class PaymentProcessingError(Exception):
    pass

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Unhandled exception in {func.__name__}: {e}', exc_info=True)
            raise e
    return wrapper
