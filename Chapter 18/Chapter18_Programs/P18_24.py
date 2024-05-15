def add_creation_time(cls):
    init = cls.__init__

    def new_init(self, *args, **kwargs):
        from time import ctime
        self.time_of_creation = ctime()
        print(f'A new object of type {cls.__name__} created')
        init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@add_creation_time
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'Hello, I am {self.name}')


@add_creation_time
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print(f'{self.model}, {self.max_speed}')


bob = Person('Bob', 23)
tom = Person('Tom', 66)

x = Car('Audi R8', 'White')
y = Car('Jaguar XJ', 'Black')

print(bob.time_of_creation)
print(tom.time_of_creation)
print(x.time_of_creation)
print(y.time_of_creation)
