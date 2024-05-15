import operator

print(list(map(lambda x, y: x * y, [1, 2, 3, 4], [5, 6, 7, 8])))
print(list(map(operator.mul, [1, 2, 3, 4], [5, 6, 7, 8])))
