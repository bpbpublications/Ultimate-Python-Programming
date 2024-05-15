L = [1, 2, -3, 4, -5, -6, 8]

i = 0
while i < len(L):
    print(i, L[i], end = ' | ')
    if L[i] < 0:
        L.remove(L[i])
    i += 1
print(L)
