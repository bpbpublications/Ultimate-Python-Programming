def gfn():
    yield 1
    yield 2
    return 10
    yield 3
    yield 4


for i in gfn():
    print(i, end=' ')
