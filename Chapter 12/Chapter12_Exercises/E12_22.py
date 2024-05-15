m = 5
n = 5


def func1():
    m = 10
    n = 10

    def func2():
        nonlocal m
        global n
        print(m, n, end=' ')

    print(m, n, end=' ')
    func2()


func1()
