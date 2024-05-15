def bubble_sort(a, compare=lambda x, y: x > y):
    for x in range(len(a) - 1, 0, -1):
        swaps = 0
        for j in range(x):
            if compare(a[j], a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
        if swaps == 0:
            break


list1 = [6, 3, 1, 5, 9, 8]
bubble_sort(list1)
print(list1)

list1 = [6, 3, 1, 5, 9, 8]
bubble_sort(list1, lambda x, y: x < y)
print(list1)

L = [('Tom', 14), ('Sam', 12), ('Ron', 19), ('Ken', 13)]
bubble_sort(L, compare=lambda t1, t2: t1[1] > t2[1])
print(L)