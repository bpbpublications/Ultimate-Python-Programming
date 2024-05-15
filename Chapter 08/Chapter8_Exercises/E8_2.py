L = [1, 2, 3, 4, 5, 6]
for i in range(0, len(L) - 1, 2):
    L[i], L[i + 1] = L[i + 1], L[i]
print(L)
