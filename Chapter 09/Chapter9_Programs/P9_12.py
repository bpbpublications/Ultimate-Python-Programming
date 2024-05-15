L = [1, 2, -3, 6, 18, -9, 12, -5, 19, -8, 5]
L1 = [n for n in L if n % 2 == 0]
print(L1)

L2 = [n if n % 2 == 0 else 0 for n in L]
print(L2)

L3 = [n if n > 0 else 0 for n in L]
print(L3)

L4 = [n // 2 if n % 2 == 0 else n * 2 for n in L if n >= 0]
print(L4)



