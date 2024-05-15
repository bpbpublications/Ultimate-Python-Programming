prices1 = {'apple': 10, 'mango': 15, 'banana': 20}
prices2 = {'grapes': 25, 'banana': 17, 'papaya': 12}
prices1.update(prices2)
print(prices1)

L = [['guava', 23], ['fig', 30], ['mango', 25]]
prices1.update(L)
print(prices1)

prices1.update(lemon=15, melon=65)
print(prices1)

d1 = {'x': 1, 'y': 2, 'c': 8}
d2 = {'a': 3, 'b': 4, 'c': 7}
print(d1 | d2)

print(d2 | d1)

d1 |= d2
print(d1)
