def accepts_only_kwargs(fn):
    def wrapper(*args, **kwargs):
        if args:
            raise ValueError('Positional arguments not allowed')
        return fn(*args, **kwargs)

    return wrapper


@accepts_only_kwargs
def func1(x, y, z):
    print(x, y, z)


# Another way of enforcing only keyword arguments
def func2(*, a, b, c, d):
    print(a, b, c, d)


func1(x=1, y=2, z=3)
#func1(1, 2, 3)  # this call will give error

func2(a=1, b=2, c=3, d=4)
#func2(1, 2, 3, 4)  # this call will give error
