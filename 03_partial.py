from functools import partial, reduce


def adder(p1, p2, a1=0, a2=0, *args, k1=0, k2=0, **kwargs):
    adder = [p1, p2, a1, a2, k1, k2]
    print("not added", args, kwargs)
    return reduce(lambda x, y: x * 10 + y, adder)


new_adder = partial(adder, 1, 2, 3, 4, k1=5, k2=6, k3=7, k4=8)
print(new_adder(7, 8, 9, 1, k1=2, k2=3, k3=4))

# not added (7, 8, 9, 1) {'k3': 4, 'k4': 8}
# 123423
