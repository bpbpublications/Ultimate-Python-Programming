from functools import wraps


def first_arg_can_be(*outer_args):
    def actual_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not args:
                raise ValueError('There should be at least one positional argument')
            if args[0] not in outer_args:
                raise ValueError(f'First argument should be one of these values {outer_args}')
            return fn(*args, **kwargs)

        return wrapper

    return actual_decorator


@first_arg_can_be(1, 2, 3, 6, 9)
def func1(x, y, z):
    print(x, y, z)


func1(6, 67, 34)
#func1(8, 67, 34)  # this call gives error


@first_arg_can_be('cut', 'copy', 'paste')
def func2(a, b):
    print(a, b)


func2('cut', 2)
#func2('yes', 2)  # this call gives error


@first_arg_can_be('user', 'admin')
def func3(m, n):
    print(m, n)


func3('admin', 2)
#func3('new', 2)  # this call gives error
