def func():
    try:
        print(3 / 0)
    except ZeroDivisionError as e:
        print('Caught a ZeroDivisionError in func : ', e)


try:
    func()
except ZeroDivisionError as e:
    print('Caught a ZeroDivisionError : ', e)


def func():
    try:
        print(3 / 0)
    except ZeroDivisionError as e:
        print('Caught a ZeroDivisionError in func : ', e)
        raise


try:
    func()
except ZeroDivisionError as e:
    print('Caught a ZeroDivsionError : ', e)
