def first_arg_string(fn):
    def wrapper(*args, **kwargs):
        if not args:
            raise ValueError('There should be at least one positional argument')
        if not isinstance(args[0], str):
            raise ValueError('First argument should be a string')
        return fn(*args, **kwargs)

    return wrapper

@first_arg_string
def func1(x, y, z):
    print(x, y, z)

func1('abcd', 2, 3)
func1(1, 2, 3)  # this call will give error
