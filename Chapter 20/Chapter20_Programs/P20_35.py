def func():
    try:
        5 / 0
    except ZeroDivisionError as excp:
        print(exc)


func()
