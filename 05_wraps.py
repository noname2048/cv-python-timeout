from functools import partial, update_wrapper, wraps


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wraps(func)(wrapper)


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


def decorator3(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return partial(update_wrapper, wrapped=func)(wrapper)


def decorator4(func):
    @partial(update_wrapper, wrapped=func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


@decorator
def say_hello(name):
    """print hello with names"""
    print(f"Hello! {name}")


@decorator2
def say_hi(name):
    """print hi with names"""
    print(f"Hi! {name}")


@decorator3
def say_morning(name):
    """print morning with names"""
    print(f"Morning! {name}")


@decorator4
def say_evening(name):
    """print evening with names"""
    print(f"Evening! {name}")


if __name__ == "__main__":
    say_hello("John")
    print(say_hello.__name__)
    print(say_hello.__doc__)
    # Something is happening before the function is called
    # Hello! John
    # Something is happening after the function is called
    # say_hello
    # print hello with names

    say_hi("John")
    print(say_hi.__name__)
    print(say_hi.__doc__)
    # Something is happening before the function is called
    # Hi! John
    # Something is happening after the function is called
    # say_hi
    # print hi with names

    say_morning("John")
    print(say_morning.__name__)
    print(say_morning.__doc__)
    # Something is happening before the function is called
    # Morning! John
    # Something is happening after the function is called
    # say_morning
    # print morning with names

    say_evening("John")
    print(say_evening.__name__)
    print(say_evening.__doc__)
    # Something is happening before the function is called
    # Evening! John
    # Something is happening after the function is called
    # say_evening
    # print evening with names
