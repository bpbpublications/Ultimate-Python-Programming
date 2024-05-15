def delay_execution(fn):
    def wrapper(*args, **kwargs):
        from time import sleep
        print(f'Please wait...{fn.__name__} will execute in a short while')
        sleep(5)
        result = fn(*args, **kwargs)
        return result

    return wrapper


@delay_execution
def func1():
    print('Hello world')


func1()
