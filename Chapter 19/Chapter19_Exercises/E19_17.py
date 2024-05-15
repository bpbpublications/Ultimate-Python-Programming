def func(f1, f2, x, y):
    return f1(x) + f2(x, y)


n = func(lambda x: x ** 2, lambda x, y: max(x, y), 4, 6)
print(n)
