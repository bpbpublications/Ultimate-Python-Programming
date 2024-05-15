L = [12, ['a', 'b']]
L1 = L * 3
print(L1)

L1[1][0] = 'z'
print(L1)
print(L)


