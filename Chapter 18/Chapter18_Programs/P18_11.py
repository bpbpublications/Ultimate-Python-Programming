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
def func1(x, n):
    return x ** n


@accepts_ints
def func2(n):
    total = 0
    for i in range(n):
        total += i
    return total


# x = func1(2, n=5.8)
x = func1(2, n=5)
y = func2(50)
print(x, y)
