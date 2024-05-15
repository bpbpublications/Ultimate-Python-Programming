L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = [x * y for x in L1 for y in L2]
L4 = [x * y for x, y in zip(L1, L2)]
print(L3, L4)
