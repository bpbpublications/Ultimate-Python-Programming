def my_decorator(fn):
    def wrapper():
        print('Hi … Starting execution')
        fn()
        print('Bye … finished executing\n')

    return wrapper


@my_decorator
def func1():
    print('Hello world')
    print('Welcome to Python')


@my_decorator
def func2():
    for i in range(10):
        print(i, end=' ')
    print()


@my_decorator
def func3():
    print('Learning decorators')


func1()
func2()
func3()
