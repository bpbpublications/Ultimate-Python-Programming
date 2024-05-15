def func():
    def f():
        nonlocal n
        n = 5

    f()
    print(n)


func()
