L = [1, 2]


def func2():
    L = [6, 7]


func2()
print(L)

L = [1, 2]


def func1():
    L.append(3)


func1()
print(L)
