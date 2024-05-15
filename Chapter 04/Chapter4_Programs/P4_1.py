L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

print(L[2:7])
print(L[2:77])
print(L[:5])
print(L[5:])
print(L[-5:])
print(L[2:9:2])
print(L[::2])
print(L[:])
print(L[::-1])

L1 = L[::-1]
L2 = L[:]
print(f'L1 is {L1}')
print(f'L2 is {L2}')
