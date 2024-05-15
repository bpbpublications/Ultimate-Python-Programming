import functools
import operator

L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]]

L1 = functools.reduce(operator.concat, L)
print(L1)

L2 = functools.reduce(operator.add, L)
print(L2)

L3 = functools.reduce(lambda x, y: x + y, L)
print(L3)

