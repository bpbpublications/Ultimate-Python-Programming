def my_decorator(fn):
    def wrapper():
        fn()

    return wrapper


def func1():
    print('Welcome to Python')


i1 = hex(id(func1))
func1 = my_decorator(func1)
i2 = hex(id(func1))
print(i1 == i2)
