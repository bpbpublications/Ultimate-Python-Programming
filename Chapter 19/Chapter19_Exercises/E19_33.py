import functools
import operator

prices = [('pen', 10), ('pencil', 3), ('eraser', 6), ('book', 60)]
s1 = functools.reduce(operator.add, map(lambda x: x[1], prices))
s2 = sum(map(lambda x: x[1], prices))
s3 = sum(x[1] for x in prices)
print(s1, s2, s3)
