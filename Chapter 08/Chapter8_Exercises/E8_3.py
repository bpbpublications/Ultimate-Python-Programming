
listA = [1, 3, 4, 8, 5, 6, 7]
list_even = []
for i in range(len(listA)):
    if listA[i] % 2 == 0:
        list_even.append(listA.pop(i))
list_odd = listA
print(list_even, list_odd)


listA = [1, 3, 4, 8, 5, 6, 7]
list_even = []
for item in listA[:]:
    if item % 2 == 0:
        list_even.append(item)
        listA.remove(item)
list_odd = listA
print(list_even, list_odd)