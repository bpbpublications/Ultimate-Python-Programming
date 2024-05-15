listA = [1, 2, 3, 4]
listB = []

while listA:
    listB.append(3 * listA.pop())

print(listA, listB)
