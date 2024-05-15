def timer(fn):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f'{fn.__name__} took {end - start} seconds')
        return result
    return wrapper


@timer
def func(n):
    print('func executing')
    return n * 2


s = func(9)
print(s)
