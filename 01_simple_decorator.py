def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello(name):
    """print hello with names"""
    print(f"Hello! {name}")


if __name__ == "__main__":
    say_hello("John")
    print(say_hello.__name__)
    print(say_hello.__doc__)
    # Something is happening before the function is called
    # Hello! John
    # Something is happening after the function is called
    # wrapper
    # None
