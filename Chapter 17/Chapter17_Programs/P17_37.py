g = (n * n * n for n in range(2, 6))

print(next(g), next(g), next(g), next(g))

g = (n * n * n for n in range(2, 6) if n % 2 == 0)
print(next(g), next(g))

for i in (n * n * n for n in range(2, 6) if n % 2 == 0):
    print(i)
