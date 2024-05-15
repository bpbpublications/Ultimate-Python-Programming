L = [2, 6, -4, 8, 3, 9, -5, -3]

d1 = {n: n ** 2 for n in L}
print(d1)

d2 = {n: n ** 2 for n in L if n > 0}
print(d2)
