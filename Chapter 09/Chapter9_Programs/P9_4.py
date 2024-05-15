L = [[1, 2, 11, 13], [12, 34, 56, 10], [13, 77, 89], [56, 78]]
L1 = [sum(sublist) for sublist in L]
print(L1)

L2 = [max(sublist) for sublist in L]
print(L2)