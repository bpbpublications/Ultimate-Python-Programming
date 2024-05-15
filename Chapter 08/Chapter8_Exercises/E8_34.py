L = [1, 2, -3, 4, -5, -6, -8]
my_list = L
for item in L[:]:
    if item < 0:
        L.remove(item)
print(L, my_list)

L = [1, 2, -3, 4, -5, -6, -8]
your_list = L
L1 = []
for item in L:
    if item >= 0:
        L1.append(item)
L = L1
print(L, your_list)
