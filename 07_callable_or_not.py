from functools import wraps


def decorator(value, *args, **kwargs):
    if callable(value):

        def wrapper(*w_args, **w_kwargs):
            print("before")
            ret = value(*w_args, **w_kwargs)
            print("after")
            return ret

        return wrapper

    value = value or "morning"

    def decorator2(func):
        def wrapper(*w_args, **w_kwargs):
            print("before", value)
            ret = func(*w_args, **w_kwargs)
            print("after", value)
            return ret

        return wrapper

    return decorator2


@decorator("12:00")
def say_hello(name):
    """print hello with names"""
    print(f"Hello! {name}")


@decorator
def say_hi(name):
    """print hi with names"""
    print(f"Hi! {name}")


say_hello("John")
say_hi("Hawk")
