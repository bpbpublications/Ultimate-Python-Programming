from functools import wraps
from time import sleep

def timer(active=True):
    def actual_decorator(fn):
        if active == True:
            @wraps(fn)
            def wrapper(*args, **kwargs):
                from time import time
                start = time()
                result = fn(*args, **kwargs)
                end = time()
                print(f'{fn.__name__} took {end - start} seconds')
                return result
            return wrapper
        else:
            return fn
    return actual_decorator

@timer(active=True)
def func1():
    sleep(2)
    print('func1 executed')

@timer(active=False)
def func2():
    sleep(3)
    print('func2 executed')

func1()
func2()

timer_option = True

@timer(active=timer_option)
def func3():
    sleep(2)
    print('func3 executed')

@timer(active=timer_option)
def func4():
    sleep(3)
    print('func4 executed')

func3()
func4()
