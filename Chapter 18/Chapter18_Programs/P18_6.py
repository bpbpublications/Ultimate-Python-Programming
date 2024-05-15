def logger(fn):
    def wrapper():
        from time import ctime
        with open('log.txt', 'a') as fout:
            fout.write(f'{fn.__name__} called at {ctime()}\n')
        fn()

    return wrapper


@logger
def func1():
    x = 999 ** 99999


@logger
def func2():
    L = [x for x in range(9999999)]


func1()
func2()
