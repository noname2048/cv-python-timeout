from functools import update_wrapper


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


def decorator_with_update(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return update_wrapper(wrapper, func)


@decorator
def say_hello(name):
    """print hello with names"""
    print(f"Hello! {name}")


@decorator_with_update
def say_hi(name):
    """print hi with names"""
    print(f"Hi! {name}")


if __name__ == "__main__":
    say_hello("John")
    print(say_hello.__name__)
    print(say_hello.__doc__)
    # Something is happening before the function is called
    # Hello! John
    # Something is happening after the function is called
    # wrapper
    # None

    say_hi("John")  # Hi! John
    print(say_hi.__name__)  # say_hi
    print(say_hi.__doc__)  # print hi with names
    # Something is happening before the function is called
    # Hi! John
    # Something is happening after the function is called
    # say_hi
    # print hello with names
