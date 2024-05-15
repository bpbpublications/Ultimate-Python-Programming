class MyError(Exception):
    pass


try:
    raise MyError
except MyError as e:
    print(e)
