L = []
for x in [2, 3, 4, 5]:
    L.append(x * 2)
print(L)

L = list(map(lambda x: x * 2, [2, 3, 4, 5]))
print(L)

L = [x * 2 for x in [2, 3, 4, 5]]
print(L)
