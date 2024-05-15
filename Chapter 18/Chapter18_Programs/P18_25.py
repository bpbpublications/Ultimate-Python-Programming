def counter(cls):
    cls.count = 0
    init = cls.__init__

    def new_init(self, *args, **kwargs):
        cls.count += 1
        self.serial_number = cls.count
        init(self, *args, **kwargs)

    cls.__init__ = new_init

    cls.__lt__ = lambda self, other: self.serial_number < other.serial_number
    cls.__gt__ = lambda self, other: self.serial_number > other.serial_number

    return cls


@counter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'Hello, I am {self.name}')


@counter
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print(f'{self.model}, {self.max_speed}')

bob = Person('Bob', 23)
tom = Person('Tom', 66)
sam = Person('Sam', 45)
jim = Person('Jim', 56)

x = Car('Audi R8', 'White')
y = Car('Jaguar XJ', 'Black')
z = Car('Toyota Glanza', 'Blue')

L = [tom, bob, jim, sam]

print(Person.count, Car.count)
print(sam.serial_number, x.serial_number)

for person in sorted(L):
    print(person.name, end=' ')

