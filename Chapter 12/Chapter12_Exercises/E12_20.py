n = 5


def func1():
    def func2():
        nonlocal n
        print(n, end=' ')

    func2()


func1()
