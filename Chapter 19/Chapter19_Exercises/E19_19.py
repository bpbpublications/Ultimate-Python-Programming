import functools
import operator

L = [('X', 4), ('Y', 5), ('H', 9), ('O', 6), ('L', 2), ('P', 7)]

r = functools.reduce(operator.mul, filter(lambda x: x % 2 == 0, map(lambda x: x[1], L)))
print(r)
