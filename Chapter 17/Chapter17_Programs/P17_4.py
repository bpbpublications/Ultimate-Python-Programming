L = ['a', 'b', 'c', 'd', 'e']
i1 = iter(L)
i2 = iter(L)
i3 = iter(L)
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i2))
print(next(i2))
print(next(i3))
print(next(i1))
print(next(i2))
print(next(i3))
