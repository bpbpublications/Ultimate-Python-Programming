def func(n):
    print('hello ' * n)


def f(x, y):
    x(y)


f(func, 4)
