def my_decorator(cls):
    if cls.__doc__ is None:
        cls.__doc__ = '\nThis is an important class\n'
    else:
        cls.__doc__ += '\nThis is an important class\n'

    cls.author = 'Ryan'
    return cls


@my_decorator
class Person:
    """This is the docstring of Person class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'Hello, I am {self.name}')

print(Person.__doc__)
print(Person.__dict__)

class Car:
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed

    def show(self):
        print(f'{self.model}, {self.max_speed}')

Car = my_decorator(Car)
print(Car.__doc__)
print(Car.__dict__)
