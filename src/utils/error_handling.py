import logging
from functools import wraps

logger = logging.getLogger(__name__)

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Error occurred in {func.__name__}: {str(e)}', exc_info=True)
            raise e
    return wrapper
