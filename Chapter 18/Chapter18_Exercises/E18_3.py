def my_decorator(fn):
    def wrapper():
        fn()
        print('@')

    return wrapper


@my_decorator
def func1():
    print('Learning Decorators', end=' ')


func1()
