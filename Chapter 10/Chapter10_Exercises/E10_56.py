def func(x, y):
    x.append(1)
    y = []


list1 = [1, 2]
list2 = [1, 2]
func(list1, list2)
print(list1, list2)
