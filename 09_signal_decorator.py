import signal
from functools import wraps


class TimeoutError(Exception):
    pass


def timeout(seconds=5):
    def decorator(func):
        def _handle_timeout(signum, frame):
            print("signum: ", signum)
            print("frame: ", frame)
            raise TimeoutError("Timeout!")

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator


@timeout()
def slow_func() -> None:
    import time

    time.sleep(10)
    print("Done!")


slow_func()
