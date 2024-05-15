def introduce_yourself(self):
    print(f'I am an instance object of {self.__class__.__name__} ')
    print(f'My id is {hex(id(self))}')
    print(f'Here are my attributes - ')
    for key, value in self.__dict__.items():
        print(f'{key} : {value}')

def introducer(cls):
    cls.introduce_yourself = introduce_yourself
    return cls

@introducer
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'Hello, I am {self.name}')


@introducer
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print(f'{self.model}, {self.max_speed}')


bob = Person('Bob', 23)
tom = Person('Tom', 66)
sam = Person('Sam', 45)

x = Car('Audi R8', 'White')
y = Car('Jaguar XJ', 'Black')
z = Car('Toyota Glanza', 'Blue')

bob.introduce_yourself()
y.introduce_yourself()
