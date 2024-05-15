from functools import wraps

def logger(log_file='log.txt'):
    def actual_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            from time import ctime
            with open(log_file, 'a') as fout:
                fout.write(f'{fn.__name__} called at {ctime()}\n')
            return fn(*args, **kwargs)

        return wrapper

    return actual_decorator


@logger()
def func1(a, b):
    print(a, b)


@logger('log2.txt')
def func2(x, y, z):
    print(x, y, z)


func1(1, 2)
func2(10, 20, 30)
func1(2, 4)
func2(1, 2, 3)
