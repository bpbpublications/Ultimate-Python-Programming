def func():
    try:
        5 / 0
    except ZeroDivisionError as excp:
        print(exc)


try:
    func()
except Exception as e:
    print(e)
    print(e.__context__)
