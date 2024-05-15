from functools import wraps


def trace(active=True):
    def actual_decorator(fn):
        if active:
            @wraps(fn)
            def wrapper(*args, **kwargs):
                print(f'{fn.__name__} called')
                print(f'args : {args}  kwargs : {kwargs}')
                result = fn(*args, **kwargs)
                print(f'Return value : {result}\n')
                return result

            return wrapper
        else:
            return fn

    return actual_decorator


@trace(active=False)
def func1(x, n):
    return x ** n


@trace()
def func2(m, n):
    return m * n


@trace(True)
def func3(m, n):
    return m + n


x = func1(2, 4)
y = func2(10, 3)
z = func3(2, 4)
print(x, y, z)
