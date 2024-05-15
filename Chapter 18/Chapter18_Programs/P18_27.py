from functools import wraps

def trace(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f'{fn.__name__} called')
        print(f'args : {args[1:]}  kwargs : {kwargs}' )
        result = fn(*args, **kwargs)
        print(f'Return value : {result}\n')
        return result
    return wrapper

def tracer(cls):
    for attr_name, value in cls.__dict__.items():
      if callable(value) and not(attr_name.startswith("__") and attr_name.endswith("__") ):
        setattr(cls, attr_name, trace(value) )
    return cls


@tracer
class MyClass:
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b

    def method1(self, x):
        return self.a + x

    def method2(self, message):
        print(message + self.name)


a = MyClass('ABC', 1, 2)
a.method1(4)
a.method2(message='Hello ')
