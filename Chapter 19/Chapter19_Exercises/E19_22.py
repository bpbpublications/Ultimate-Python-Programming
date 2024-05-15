from functools import reduce

print(reduce(lambda a, b: a if a > b else b, [4, 3, 2, 7, 6]))
print(reduce(lambda a, b: a if a < b else b, [4, 3, 2, 7, 6]))

print(max([4, 3, 2, 7, 6]))
print(min([4, 3, 2, 7, 6]))