def returns(*o_args):
    def actual_decorator(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            if not isinstance(result, o_args):  # isinstance can take a tuple as the second argument
                raise ValueError(f'Return value should be one of these types {o_args}')
            return result

        return wrapper

    return actual_decorator


@returns(int, float)  # function can return an int or float only
def func1():
    return 1.2


@returns(list, tuple)  # function can return a list or tuple only
def func2():
    return [1, 3]


@returns(str)  # function can return a string only
def func3():
    return 'xy'


a = func1()
b = func2()
c = func3()
