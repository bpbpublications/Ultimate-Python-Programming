d = {'a': [1, 2, 3], 'b': 10, 'c': 12}
d2 = d
d['a'][1] = 55
d['b'] = 99
print(d2)
