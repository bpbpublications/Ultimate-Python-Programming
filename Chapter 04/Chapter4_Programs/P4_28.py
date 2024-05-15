L = [1, 2, 3, 4]
L1 = L  # makes an alias
L2 = L[:]  # makes a copy by slice notation
L3 = list(L)  # makes a copy by list function
L4 = L.copy()

print(L, L1, L2, L3, L4)
print(id(L), id(L1), id(L2), id(L3), id(L4))

L2[0] = 35
print(L2, L)

L3.append(45)
print(L3,L)

L4[1] += 100
print(L4,L)

L1[0] = 99
print(L1, L)

L[1] = 1000
print(L, L1)

