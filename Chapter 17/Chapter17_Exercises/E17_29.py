def gfn(n):
    for i in range(n, 1, -1):
        yield i
    for i in range(1, n + 1):
        yield i


for i in gfn(5):
    print(i, end=' ')
