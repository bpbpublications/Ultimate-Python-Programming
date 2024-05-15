def func():
    def f():
        nonlocal x
        x = 10
    f()
    print(x)

func()
