def func():
    print('Hello')


x = func
del func
x()