def delay_execution(seconds):
    def actual_decorator(fn):
        def wrapper(*args, **kwargs):
            from time import sleep
            print(f'Please wait...{fn.__name__} will execute in a short while')
            sleep(seconds)
            result = fn(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


@delay_execution(3)
def func1():
    print('Hello world')


@delay_execution(2)
def func2():
    print('Hi world')


func1()
func2()
