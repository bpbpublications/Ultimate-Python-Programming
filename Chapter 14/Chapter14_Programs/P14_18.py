class Person:
    species = 'Homo sapien'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'{self.name} is {self.age} years old {Person.species}')


p1 = Person('John', 20)
p2 = Person('Jack', 34)

p1.display()
p2.display()
