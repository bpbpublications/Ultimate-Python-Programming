def cannot_return_zero(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result == 0:
            raise ValueError('Return value cannot be zero')
        return result

    return wrapper

@cannot_return_zero
def func1(x, y):
    return x + y

a = func1(2, 3)
#b = func1(2, -2)  # this call will give error
