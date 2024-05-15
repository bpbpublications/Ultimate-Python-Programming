def func(x, y):
    print(x, y)
    print(id(x), id(y))


num = 2
my_list = [1, 2, 3]
print(id(num), id(my_list))
func(num, my_list)