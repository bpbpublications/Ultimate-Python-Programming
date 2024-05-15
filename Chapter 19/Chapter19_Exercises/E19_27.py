L = []
for x in [2, 3, 4, 5]:
    if x % 2 == 0:
        L.append(x)
print(L)

L = list(filter(lambda x: x % 2 == 0, [2, 3, 4, 5]))
print(L)

L = [x for x in [2, 3, 4, 5] if x % 2 == 0]
print(L)
