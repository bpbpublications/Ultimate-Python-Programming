L = [('Ted', 23), ('Lee', 18), ('Sam', 22), ('Bob', 30), ('Dev', 27), ('Ray', 25)]
L1 = [name for name, bmi in L if 20 < bmi < 26]
print(L1)
