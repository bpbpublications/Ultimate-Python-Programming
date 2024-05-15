from itertools import chain

L = [1, 2]
s = {7, 8, 9}
for i in chain(L, s):
    print(i, end=' ')
