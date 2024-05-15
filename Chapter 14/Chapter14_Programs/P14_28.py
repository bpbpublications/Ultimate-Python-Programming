class Person:
    species = 'Homo sapien'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def display(self):
        print(f'{self.name} is {self.age} years old {Person.species}')

    @classmethod
    def show_count(cls):
        print(f'There are {cls.count} {cls.species}s')


Person.show_count()
p1 = Person('Devanshi', 18)
p2 = Person('Devank', 10)
Person.show_count()
