a = 10


def func():
    global a
    a = 20
    print(a, end=' ')


func()
print(a, end=' ')
