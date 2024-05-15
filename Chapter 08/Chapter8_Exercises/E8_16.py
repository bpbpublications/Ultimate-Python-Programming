L = [1, 2, 3, -5, 6, 7]
for i in L:
    if i < 0:
        L.insert(L.index(i), 0)
print(L)
