def gen_fn():
    n = 0
    print('ABC', n)
    n += 2
    yield 10
    print('GHI', n)
    print('XYZ')
    yield 20
    print('JKL', n)
    n *= 5
    yield 30
    print('MNO', n)

g = gen_fn()
v = next(g)
print(v)
v = next(g)
print(v)
v = next(g)
print(v)
v = next(g)
print(v)
v = next(g)
print(v)
