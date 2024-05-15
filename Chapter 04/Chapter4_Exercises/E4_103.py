L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(id(L1))
L1 = L1 + L2
print(L1)
print(id(L1))

L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(id(L1))
L1.extend(L2)
print(L1)
print(id(L1))
