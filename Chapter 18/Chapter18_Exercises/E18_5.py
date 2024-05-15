def my_decorator(fn):
    def wrapper(s):
        return tuple(fn(s))

    return wrapper


@my_decorator
def func1(s):
    return s.split()


print(func1('Welcome to Python'))
