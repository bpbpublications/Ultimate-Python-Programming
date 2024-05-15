n = 5


def func1():
    n = 10

    def func2():
        n = 15
        print(n, end=' ')

    print(n, end=' ')
    func2()


func1()
print(n, end=' ')
