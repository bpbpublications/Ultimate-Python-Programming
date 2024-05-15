def func():
    x = 100

    def f():
        print(x)

    f()
    print(x)


func()
