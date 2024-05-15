from functools import reduce

L = ['pen', 'pencil', 'book', 'eraser']
s1 = reduce(lambda x, y: x + ', ' + y, L)
print(s1)

s2 = ', '.join(s for s in L)
print(s2)
