import sys

try:
    f = open('xyz')
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(exc_type)
    print(exc_value)
    print(exc_traceback)
