from functools import wraps
def trace(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f'{fn.__name__} called')
        print(f'args : {args}  kwargs : {kwargs}' )
        result = fn(*args, **kwargs)
        print(f'Return value : {result}\n')
        return result
    return wrapper

def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        fn(*args, **kwargs)
        end = time()
        print(f'{fn.__name__} took {end - start} seconds')
    return wrapper

class MyClass:
    def __init__(self, a):
        self.a = a

    @timer
    def method1(self, x, y):
        print('method1 executing')

    @timer
    def method2(self, x, y):
        print('method2 executing')

    @trace
    def method3(self, x, y):
        print('method3 executing')

x = MyClass(10)
x.method1(1, 2)
x.method2(2, 4)
x.method3(3, 5)

