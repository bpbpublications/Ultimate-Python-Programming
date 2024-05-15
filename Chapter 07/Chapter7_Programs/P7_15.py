L = [(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64)]
for i, isquare, icube in L:
    print(i, isquare, icube)

for i, _, icube in L:
    print(i, icube)
