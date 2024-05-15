def cubes(start):
    n = start
    while True:
        yield n * n * n
        n = n + 1


y = cubes(2)

print(next(y), next(y))
print(next(y), next(y))
print(next(y), next(y))
print(next(y), next(y))