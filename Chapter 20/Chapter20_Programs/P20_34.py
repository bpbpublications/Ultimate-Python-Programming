def func():
    try:
        5 / 0
    except ZeroDivisionError as excp:
        raise RuntimeError('An error occurred') from excp


try:
    func()
except RuntimeError as e:
    print(e)
    print(e.__cause__)
