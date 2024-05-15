def func(a, n):
    if n == 0:
        return 1
    else:
        return a * func(a, n - 1)


print(func(3, 2), func(4, 3), func(5, 1))

