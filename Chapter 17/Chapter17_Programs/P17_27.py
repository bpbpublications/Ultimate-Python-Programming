from itertools import accumulate

L = [1, 2, 3, 4, 5, 6]
for i in accumulate(L):
    print(i, end=' ')
