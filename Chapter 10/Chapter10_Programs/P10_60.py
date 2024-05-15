def func(a, b, *args, c, d):
    print(a, b, args, c, d)


func(2, 3, 6, 7, 8, 9, c=100, d=200)


def func(a, b, *, c, d):
    print(a, b, c, d)


func(2, 3, c=100, d=200)


def func(*, a, b, c, d):
    print(a, b, c, d)


func(a=1, b=1, c=3, d=5)
