def func():
    x = 100
    def f():
       nonlocal x
       x = 30
       print(x)
    f()
    print(x)

func()
