x = 5


def func():
    x = 10
    print(x)
    print(globals()['x'])
    globals()['x'] = 20


func()
print(x)
