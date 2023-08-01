import signal
import time
from functools import wraps


class TimeoutError(Exception):
    pass


def handle_timeout(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
    raise TimeoutError


signal.signal(signal.SIGALRM, handle_timeout)
signal.alarm(5)
time.sleep(10)

print("DONE!")
