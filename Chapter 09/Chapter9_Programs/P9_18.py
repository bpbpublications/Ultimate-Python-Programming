L1 = [[]] * 3
L2 = [[0] * 3] * 4
print(L1)
print(L2)

L1[0].append(9)
print(L1)

L2[1].pop()
print(L2)

L3 = [[] for i in range(3)]
L4 = [[0] * 3 for i in range(4)]
print(L3)
print(L4)

L3[0].append(9)
print(L3)

L4[1].pop()
print(L4)
