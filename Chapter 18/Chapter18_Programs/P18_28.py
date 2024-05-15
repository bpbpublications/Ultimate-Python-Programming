class MyDecorator:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print('Decoration before execution of function')
        self.fn(*args, **kwargs)
        print('Decoration after execution of function\n')


def func(message, name):
    print(message, name)


func = MyDecorator(func)
print(func)
func('hello', 'bob')
func('hi', 'tom')

