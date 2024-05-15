x = 100

def func():
    x = 50

    def f():
        x = 20
        print(x)
    f()

func()
