def add_attrs(**kwargs):
    def actual_decorator(fn):
        for key, value in kwargs.items():
            setattr(fn, key, value)
        return fn

    return actual_decorator


@add_attrs(author='Jack', x=19)
def func1():
    pass


@add_attrs(author='Jill', a=10, y=12)
def func2():
    pass


@add_attrs(version='2.5')
def func3():
    pass


print(func1.__dict__)
print(func2.__dict__)
print(func3.__dict__)
