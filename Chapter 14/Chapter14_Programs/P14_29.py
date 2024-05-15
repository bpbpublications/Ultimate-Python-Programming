class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_str(cls, s):
        name, age = s.split(',')
        return cls(name, int(age))

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['age'])

    def display(self):
        print(f'{self.name} is {self.age} years old')


s = 'Jack, 23'
d = {'name': 'Jane', 'age': 34}
p3 = Person.from_str(s)
p3.display()

p4 = Person.from_dict(d)
p4.display()
