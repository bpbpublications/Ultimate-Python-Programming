import sys


def func():
    3 / 0
    #3 + 'x'


try:
    func()
except OSError as e:
    print(e)
    # code for handling OSError
except ValueError as e:
    print(e)
    # Code for handling ValueError
except ZeroDivisionError as e:
    print(e)
    # Code for handling ZeroDivisionError
except:
    print('An unexpected error occurred', sys.exc_info()[0])
    raise
