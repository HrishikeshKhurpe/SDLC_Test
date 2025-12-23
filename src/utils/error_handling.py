import logging
from functools import wraps

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Error occurred in {func.__name__}: {str(e)}', exc_info=True)
            raise e
    return wrapper
