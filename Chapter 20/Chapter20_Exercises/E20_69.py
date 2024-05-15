import sys


class MyError(Exception):
    pass


def func(m, n):
    try:
        print(m / n)
        import math
        print(math.exp(m))
    except (ZeroDivisionError, FloatingPointError, OverflowError) as excp:
        raise MyError('An error occurred') from excp


try:
    func(1, 0)
except MyError as e:
    print(e)
    with open('logfile.txt', 'a') as f:
        f.write(str(e.__cause__) + '\n')
        f.write(str(sys.exc_info()) + '\n')
