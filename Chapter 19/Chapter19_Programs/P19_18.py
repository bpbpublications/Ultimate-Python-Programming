list1 = [1, 9, 3, 4]
list2 = [4, 3, 6, 1, 7, 8]
list3 = [8, 9, 3, 5, 6]
print(list(map(lambda x, y, z : x + y + z, list1, list2, list3)))
