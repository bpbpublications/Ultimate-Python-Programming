L1 = [1, 2, 3, 4, 5]
L2 = [4, 6, 7, 1, 8]
L3 = [7, 5, 3, 1, 2]
L = [x + y + z for x, y, z in zip(L1, L2, L3)]
print(L)
