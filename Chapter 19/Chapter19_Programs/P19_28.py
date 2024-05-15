from functools import reduce

L = [4, 6, 3, 1, 2]


def add(x, y):
    return x + y


print(reduce(add, L))
print(reduce(add, L, 1000))
print(reduce(lambda x, y: x if x > y else y, L))

words = ['apple', 'boy', 'cat']
print(reduce(add, words))
print(reduce(lambda x, y: x + y, words))

L.clear()
print(reduce(add, L, 0))
