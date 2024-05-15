def timer(fn):
    def wrapper():
        from time import time
        start = time()
        fn()
        end = time()
        print(f'{fn.__name__} took {end - start} seconds')

    return wrapper


def func1():
    x = 999 ** 99999


def func2():
    L = [x for x in range(9999999)]


def func3():
    x = (66 * 9999) ** 99988


@timer
def func1():
    x = 999 ** 99999


@timer
def func2():
    L = [x for x in range(9999999)]


@timer
def func3():
    x = (66 * 9999) ** 99988


func1()
func2()
func3()
