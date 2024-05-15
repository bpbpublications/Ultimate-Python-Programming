L = [3, 5, 7, 1, 8, 9, 4]
cubes = [n ** 3 for n in L if n % 2 == 0]
print(cubes)

cubes = []
for n in L:
    if n % 2 == 0:
        cubes.append(n ** 3)
print(cubes)
