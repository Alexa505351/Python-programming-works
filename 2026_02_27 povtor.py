import functools
import sys

def retry(count=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(1, count + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except ValueError as e:
                    last_exception = e
                    if attempt < count:
                        continue
                    else:
                        raise
                except OSError as e:
                    print(f"{func.__name__} raise OsError exception.",
                          file=sys.stdout)
                    last_exception = e
                    if attempt < count:
                        continue
                    else:
                        raise
                except Exception as e:
                    raise
            
            if last_exception:
                raise last_exception
        
        return wrapper
    return decorator
