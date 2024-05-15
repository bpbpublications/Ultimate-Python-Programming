import functools

L = [[1, 'Agra', 3], [4, 'Delhi', 6], [7, 'Belmont', 9], [6, 'Bareilly', 3]]
s1 = functools.reduce(lambda x, y: x + '-' + y, map(lambda x: x[1], L))
print(s1)

s2 = '-'.join(x[1] for x in L)
print(s2)
