import time
from functools import wraps


def timing(func):
    """Decorator to print the runtime of the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # high-resolution timer
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper
