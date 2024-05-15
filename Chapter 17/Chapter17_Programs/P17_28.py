from itertools import zip_longest

L1 = [1, 2, 3]
L2 = [10, 20, 30, 40, 50]

print(list(zip(L1, L2)))

print(list(zip_longest(L1, L2)))

print(list(zip_longest(L1, L2, fillvalue=0)))
