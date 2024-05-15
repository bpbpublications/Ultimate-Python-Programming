from functools import wraps


class Logger():
    def __init__(self, log_file='log.txt'):
        self.log_file = log_file

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            from time import ctime
            with open(self.log_file, 'a') as fout:
                fout.write(f'{fn.__name__} called at {ctime()}\n')
            return fn(*args, **kwargs)

        return wrapper


@Logger()
def func1(a, b):
    print(a, b)


@Logger('log2.txt')
def func2(x, y, z):
    print(x, y, z)


func1(1, 2)
func2(10, 20, 30)
