def func():
    x = 100
    def f():
        x = 30
        print(x)
    f()
    print(x)

func()
