L = [-2, 1, -4, 21, 20, -3, -7, 9, 0]
L1 = [n for n in L if n < 0] + [n for n in L if n >= 0]
print(L1)
