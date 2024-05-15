import math

L1 = [10, 20, 30, 40, 70]
L2 = [2, 0, 2, 0, 7]

for m, n in zip(L1, L2):
    try:
        print(m / n)
    except ZeroDivisionError:
        print(m)
