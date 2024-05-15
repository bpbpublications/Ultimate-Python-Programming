L1 = [1, 2, 3]
print(id(L1))
L1 = L1 + [5, 6, 7]
print(L1)
print(id(L1))

L2 = [1, 2, 3]
print(id(L2))
L2 += [5, 6, 7]
print(L2)
print(id(L2))
