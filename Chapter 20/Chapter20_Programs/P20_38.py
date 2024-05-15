class MyError(Exception):
    pass

try:
    raise MyError('MyError exception raised', 1, 2, 3)
except MyError as e:
     print(e)
