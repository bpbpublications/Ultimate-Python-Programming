def limit_return_value(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result < 0 or result > 1000:
            raise ValueError('Value returned is not within limits')
        return result

    return wrapper


@limit_return_value
def func1(x, n):
    return x ** n


@limit_return_value
def func2(n):
    total = 0
    for i in range(n):
        total += i
    return total


x = func1(2, 5)
print(x)
y = func2(600)
print(y)
