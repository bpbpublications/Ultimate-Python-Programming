numbers = [24, 34, 0, 4, 12, 45, 67, 15]


def func(x):
    return x % 3 == 0


print(list(filter(func, numbers)))
print(list(filter(lambda x : x % 3 == 0, numbers)))
print(list(filter(None, numbers)))