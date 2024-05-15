listA = [15, 2, 4, 3, 8, 9]
for i in range(len(listA)):
    listA[i] = listA[i] // 2 if listA[i] % 2 == 0 else listA[i] * 2
print(listA)
