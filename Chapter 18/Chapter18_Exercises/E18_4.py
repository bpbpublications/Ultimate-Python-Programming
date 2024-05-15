def my_decorator(fn):
    def wrapper(s):
        fn(s)

    return wrapper


@my_decorator
def func1(s):
    return s.upper()


print(func1('abcd'))
