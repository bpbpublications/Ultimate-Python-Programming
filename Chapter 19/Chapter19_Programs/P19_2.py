def func(x):
    if x < 0:
        return lambda: print('Hello')
    elif x > 0:
        return lambda: print('Hi')
    else:
        return lambda: print('Hey')


f1 = func(6)
f1()
f2 = func(0)
f2()
