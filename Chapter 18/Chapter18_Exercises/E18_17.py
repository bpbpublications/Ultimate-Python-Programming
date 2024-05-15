def timer(fn):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f'{fn.__name__} took {end - start} seconds')
        return result

    return wrapper


sum = timer(sum)
x = sum([x for x in range(999999)])
print(x)
