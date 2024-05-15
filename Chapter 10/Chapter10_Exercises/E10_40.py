my_dict = {1: 'a', 2: 'b', 3: 'c'}


def func(d):
    d = {}
    d[1] = 100


func(my_dict)
print(my_dict)
