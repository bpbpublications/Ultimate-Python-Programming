def limit_return_value(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result < 0 or result > 1000:
            raise ValueError('Value returned is not within limits')
        return result

    return wrapper


def accepts_ints(fn):
    def wrapper(*args, **kwargs):
        arguments = args
        arguments += tuple(kwargs.values())

        for argument in arguments:
            if not isinstance(argument, int):
                raise TypeError('This function accepts only integer arguments')
        result = fn(*args, **kwargs)
        return result

    return wrapper


@accepts_ints
@limit_return_value
def func1(x, n):
    return x ** n


# x = func1(2, n=5.8)
# x = func1(2, n=59)
x = func1(2, n=5)
print(x)
