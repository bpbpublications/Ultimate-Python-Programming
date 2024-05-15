def func1():
    print('Hello world')
    print('Welcome to Python')


def my_decorator(fn):
    def wrapper():
        print('Hi … Starting execution')
        fn()
        print('Bye … finished executing\n')

    return wrapper


decorated_func1 = my_decorator(func1)
decorated_func1()

func1 = my_decorator(func1)
func1()
