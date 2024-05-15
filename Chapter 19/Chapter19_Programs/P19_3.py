def func(x, username):
    if x < 0:
        return lambda: print('Hello', username)
    elif x > 0:
        return lambda: print('Hi', username)
    else:
        return lambda: print('Hey', username)


f1 = func(6, 'Sam')
f1()
f2 = func(0, 'Tim')
f2()
