L = [1, 2, 3, 2, 4, 5, 2, 2, 2, 7]
x = 2
for item in L[:]:
    if item == x:
        L.remove(item)
print(L)

L = [1, 2, 3, 2, 4, 5, 2, 2, 2, 7]
x = 2
while x in L:
    L.remove(x)
print(L)
