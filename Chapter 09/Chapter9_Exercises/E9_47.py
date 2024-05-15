L1 = [x * y for x in [3, 6, 7] for y in [4, 5, 6]]
L2 = [[x * y for x in [3, 6, 7]] for y in [4, 5, 6]]
print(L1, L2)

L1 = []
for x in [3, 6, 7]:
    for y in [4, 5, 6]:
        L1.append(x * y)

L2 = []
for y in [4, 5, 6]:
    temp = []
    for x in [3, 6, 7]:
        temp.append(x * y)
    L2.append(temp)

print(L1, L2)