L = [32, -51, 63, 11, 86, -9, 66, 88, 97]
L1 = [n * 2 for n in L if n > 0]
print(L1)

evens = [n for n in L if n % 2 == 0]
odds = [n for n in L if n % 2 != 0]
print(evens)
print(odds)
