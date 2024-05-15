def func():
    try:
        print(4 + 'x')
    except TypeError as e:
        print('Caught a TypeError in func : ', e)
func()


def func():
    try:
        print(4+'x')
    except TypeError as e:
        print('Caught a TypeError in func : ', e)
        raise
func()
