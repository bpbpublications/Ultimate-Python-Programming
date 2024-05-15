import functools
import operator

L = [1, 2, 3]

print(functools.reduce(operator.add, L, 322))

print(322 + sum(L))
