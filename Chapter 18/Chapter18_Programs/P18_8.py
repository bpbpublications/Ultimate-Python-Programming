def timer(fn):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        fn(*args, **kwargs)
        end = time()
        print(f'{fn.__name__} took {end - start} seconds')

    return wrapper


@timer
def func1():
    L = [x for x in range(999999)]


@timer
def func2(n):
    total = 0
    for i in range(n):
        total += i
    print(total)


func1()
func2(999999)
