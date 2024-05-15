names = ['John', 'Joe', 'Ted', 'Sam', 'Jack', 'Jill']
heights = [160, 152, 147, 167, 177, 182]
weights = [54, 60, 90, 77, 87, 67]

L = [(name, (wt / (ht * ht * 0.0001))) for name, ht, wt in zip(names, heights, weights)]
print(L)