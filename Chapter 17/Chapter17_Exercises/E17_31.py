def combine(a, b, c):
    for i in a:
        yield i
    for i in b:
        yield i
    for i in c:
        yield i


L = [1, 2, 3, 4, 5]

for i in combine(L, range(10, 15), 'ABCDEF'):
    print(i, end=' ')



