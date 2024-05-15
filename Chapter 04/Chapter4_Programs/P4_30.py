from copy import deepcopy

L = [12, 13, ['a', 'b']]
L2 = L.copy()
L3 = deepcopy(L)

print(id(L[2]), id(L2[2]), id(L3[2]))
L3[2].append('c')
print(L3)
print(L)

