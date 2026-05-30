import functools

def retry(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    continue
                except OSError:
                    print(f"{func.__name__} raise OsError exception.")
                    continue
            return func(*args, **kwargs)
        return wrapper
    return decorator
