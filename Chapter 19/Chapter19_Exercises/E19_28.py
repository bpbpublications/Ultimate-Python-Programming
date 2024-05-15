L = []
for x in [2, 3, 4, 5, 6, 7]:
    if x % 2 == 0:
        L.append(x ** 3)
print(L)

L = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, [2, 3, 4, 5, 6, 7])))
print(L)

L = [x ** 3 for x in [2, 3, 4, 5, 6, 7] if x % 2 == 0]
print(L)