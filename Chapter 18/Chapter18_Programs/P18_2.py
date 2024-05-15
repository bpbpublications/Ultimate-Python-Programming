def func1():
    print('Hello world')
    print('Welcome to Python')


def func2():
    for i in range(10):
        print(i, end=' ')
    print()


def func3():
    print('Learning decorators')


def my_decorator(fn):
    def wrapper():
        print('Hi … Starting execution')
        fn()
        print('Bye … finished executing\n')

    return wrapper


func1 = my_decorator(func1)
func2 = my_decorator(func2)
func3 = my_decorator(func3)

func1()
func2()
func3()
