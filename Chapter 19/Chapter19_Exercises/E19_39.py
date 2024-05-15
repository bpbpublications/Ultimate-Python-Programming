from functools import reduce
import math

n = 5
print(reduce(lambda x, y: x * y, range(1, n + 1)))

n = 6
print(reduce(lambda x, y: x * y, range(1, n + 1), 1))

n = 0
print(reduce(lambda x, y: x * y, range(1, n + 1), 1))

n = 5
print(math.prod(range(1, n + 1)))