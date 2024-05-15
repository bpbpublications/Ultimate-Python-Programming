data1 = {1: 'a', 2: 'b', 3: 'c'}
data2 = {1: 11, 2: 22, 3: 33}


def func(d):
    d[2] = 'xxxx'


func(data1)
func(data2.copy())

print(data1, data2)
