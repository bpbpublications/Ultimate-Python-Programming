import functools
import operator
import math

L = [('X', 4), ('Y', 5), ('H', 9), ('O', 6), ('L', 2), ('P', 7)]

r1 = functools.reduce(operator.mul, filter(lambda x: x % 2 == 0, map(lambda x: x[1], L)))
r2 = math.prod(x[1] for x in L if x[1] % 2 == 0)

print(r1, r2)
