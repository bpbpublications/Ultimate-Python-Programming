from functools import wraps


def limit_return_value(fn, lower_limit, upper_limit):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result < lower_limit or result > upper_limit:
            raise ValueError('Value returned is not within limits')
        return result

    return wrapper


def func2(m, n):
    return m + n


func2 = limit_return_value(func2, 100, 500)
# func2(2, 90)
func2(20, 90)
