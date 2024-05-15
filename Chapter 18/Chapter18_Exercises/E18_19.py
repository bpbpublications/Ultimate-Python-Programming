def add_to_docstring(string):
    def actual_decorator(fn):
        if fn.__doc__:
            fn.__doc__ += string
        else:
            fn.__doc__ = string
        return fn

    return actual_decorator


@add_to_docstring('\nThis function takes time to execute\n')
def func1():
    """docstring of function func1"""
    pass


@add_to_docstring('\nOnly admins can access this function\n')
def func2():
    """docstring of function func2"""
    pass


print(func1.__doc__)
print(func2.__doc__)
