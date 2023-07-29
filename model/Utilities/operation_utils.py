import time


def sleep_decorator(prefix_duration=None, postfix_duration=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if prefix_duration is not None:
                time.sleep(prefix_duration)  # Perform the prefix operation (sleep before)
            result = func(*args, **kwargs)
            if postfix_duration is not None:
                time.sleep(postfix_duration)  # Perform the postfix operation (sleep after)
            return result
        return wrapper
    return decorator