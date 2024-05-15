def cubes(start, stop):
    for n in range(start, stop + 1):
        yield n * n * n

y = cubes(2, 5)

for i in y:
    print(i)




