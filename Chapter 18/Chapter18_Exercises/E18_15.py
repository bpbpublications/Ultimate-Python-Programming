def add_to_docstring(fn):
    if fn.__doc__:
        fn.__doc__ += '\nThis line added to the docstring\n'
    else:
        fn.__doc__ = '\nThis line added to the docstring\n'
    return fn

@add_to_docstring
def func1():
    """docstring of function func1"""
    pass

@add_to_docstring
def func2():
    pass

print(func1.__doc__)
print(func2.__doc__)
