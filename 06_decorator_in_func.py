from functools import wraps


def decorator1() -> callable:
    def decorator2() -> callable:
        def decorator3() -> callable:
            def decorator4(func4) -> callable:
                def wrapper1(*args1, **kwargs1):
                    print("wrapper1 before")
                    ret = func4(*args1, **kwargs1)
                    print("wrapper1 after")
                    return ret

                return wrapper1

            return decorator4

        return decorator3()

    return decorator2()


@decorator1()
def sleep_and_print():
    import time

    time.sleep(5)
    print("Done!")


sleep_and_print()
