from functools import wraps

class MyDecorator:
    def __init__(self, fn):
        self.fn = fn
        wraps(fn)(self)
        self.author = 'Jim'  # Add a new attribute here

    def __call__(self, *args, **kwargs):
        print('Decoration before execution of function')
        result = self.fn(*args, **kwargs)
        print('Decoration after execution of function\n')
        return result

@MyDecorator
def func(message, name):
    print(message, name)
    return message + ' ' + name + '!'

x = func('hello', 'bob')
y  = func('hi', 'tom')
print(x, y)
print(func.author)
print(func.__name__)
