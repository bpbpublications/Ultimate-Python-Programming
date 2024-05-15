from functools import wraps

class Logger():
    log_file = 'log.txt'

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        from time import ctime
        with open(Logger.log_file, 'a') as fout:
            fout.write(f'{self.fn.__name__} called at {ctime()}\n')
        return self.fn(*args, **kwargs)


@Logger
def func1(a, b):
    print(a, b)


@Logger
def func2(x, y, z):
    print(x, y, z)


func1(1, 2)
func2(10, 20, 30)

Logger.log_file = 'log2.txt'

func1(3, 4)
func2(7, 8, 9)
