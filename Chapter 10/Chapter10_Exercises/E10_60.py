def func1(x, y):
    def f(a, b):
        return a + b

    return f(x, y)


def func2(x, y):
    def f(a, b):
        return a + b

    return f


j = func1(2, 3)
k = func2(2, 3)

print(type(j), type(k))

