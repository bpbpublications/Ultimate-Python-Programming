class Person:
    species = 'Homo sapien'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count += 1

    def display(self):
        print(f'{self.name} is {self.age} years old {Person.species}')


p1 = Person('Devanshi', 18)
p2 = Person('Devank', 10)
print(Person.count, p1.count, p2.count)
