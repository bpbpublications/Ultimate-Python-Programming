from functools import wraps


def limit_return_value(lower_limit, upper_limit):
    def actual_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            if result < lower_limit or result > upper_limit:
                raise ValueError('Value returned is not within limits')
            return result

        return wrapper

    return actual_decorator


@limit_return_value(0, 1000)
def func1(x, n):
    return x ** n


@limit_return_value(100, 500)
def func2(m, n):
    return m + n


def func3(x, n):
    return x * n


func3 = limit_return_value(0, 5000)(func3)

func1(5, 2)
func2(50, 200)
func3(50, 20)

# func1(5, 10)
# func2(50, 2)
# func3(50, 200)
