def func(a):
    return [i * i for i in a]


L = list(range(100))
for i in func(L):
    print(i)


def gfunc(a):
    for i in a:
        yield i * i


L = list(range(100))
for i in gfunc(L):
    print(i)
