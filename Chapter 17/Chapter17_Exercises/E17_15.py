L = [1, 2, 3]
x = iter(L)

print(next(x), end=' ')
L[2] = 300
print(next(x), next(x))
