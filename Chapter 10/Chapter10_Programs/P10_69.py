def func(x):
    if x < 0:
        def fn():
            print('Hello')
    elif x > 0:
        def fn():
            print('Hi')
    else:
        def fn():
            print('Hey')
    return fn

f = func(6)
f()
