def show_attributes(fn):
    attributes = ['__annotations__', '__defaults__', '__module__', '__name__', '__repr__',
                  '__sizeof__', '__str__']

    for attribute in attributes:
        print(attribute, '->', getattr(fn, attribute))
        print()


def func(a, b, c=1, d=2):
    print(a, b, c, d)


def divide(a, b):
    print(a // b)


show_attributes(func)
show_attributes(divide)
