list1 = [['a', 1], ['b', 2], ['c', 3]]
d1 = dict(list1)
print(d1)

t1 = ('x', 4), ('y', 5), ('z', 6)
d2 = dict(t1)
print(d2)

t2 = ['x', 4], ['y', 5], ['z', 6]
d3 = dict(t2)
print(d3)

d4 = dict((['x', 4], ['y', 5], ['z', 6]))
print(d4)

d5 = dict(['X1', 'Y2', 'Z3'])
print(d5)

d6 = dict(pencil=12, eraser=45, sharpener=30)
print(d6)

countries = ['France', 'Austria', 'Japan', 'India']
capitals = ['Paris', 'Vienna', 'Tokyo', 'New Delhi']
d7 = dict(zip(countries, capitals))
print(d7)

d8 = dict()
print(d8)
