def my_decorator(fn):
    def wrapper():
        print('Hello', end=' ')
        fn()

    return wrapper


@my_decorator


def func1():
    print('Welcome to Python')


func1 = my_decorator(func1)
func1()
