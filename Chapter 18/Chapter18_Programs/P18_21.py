from math import factorial
from random import randint


def trace(fn):
    def wrapper(*args, **kwargs):
        print(f'{fn.__name__} called')
        print(f'args : {args}  kwargs : {kwargs}')
        result = fn(*args, **kwargs)
        print(f'Return value : {result}\n')
        return result

    return wrapper


factorial = trace(factorial)
randint = trace(randint)
factorial(3)
randint(5, 50)