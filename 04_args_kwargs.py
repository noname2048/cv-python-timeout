def func1(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)
    # args (1, 2, 3, 4, 5, 6)
    # kwargs {'a': 'a', 'b': 'b'}


def func2(a, b, c, d, *args, **kwargs):
    print("a, b, c, d", a, b, c, d)
    print("args", args)
    print("kwargs", kwargs)
    # TypeError: func2() got multiple values for argument 'a'


def func3(i, j, k, l, *args, **kwargs):
    print("i, j, k, l", i, j, k, l)
    print("args", args)
    print("kwargs", kwargs)
    # i, j, k, l 1 2 3 4
    # args (5, 6)
    # kwargs {'a': 'a', 'b': 'b'}


func1(1, 2, 3, 4, 5, 6, a="a", b="b")
func2(1, 2, 3, 4, 5, 6, a="a", b="b")
func3(1, 2, 3, 4, 5, 6, a="a", b="b")
