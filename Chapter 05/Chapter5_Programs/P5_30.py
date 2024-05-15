d1 = {'a': 15, 'b': 22, 'c': 35, 'd': 24}
d2 = {'a': 15, 'b': 20, 'x': 29, 'd': 24}
print(d1.items() & d2.items())
print(d1.keys() - d2.keys())

