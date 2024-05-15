from functools import wraps


class MyDecorator:
    def __init__(self, fn):
        self.fn = fn
        wraps(fn)(self)

    def __call__(self, *args, **kwargs):
        print('Decoration before execution of function')
        self.fn(*args, **kwargs)
        print('Decoration after execution of function\n')


@MyDecorator
def func(message, name):
    print(message, name)


func('hello', 'bob')
func('hi', 'tom')
print(func.__name__)
