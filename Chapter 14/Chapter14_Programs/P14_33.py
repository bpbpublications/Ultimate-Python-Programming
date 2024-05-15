
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 20 <= new_age <= 80:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 80')

    def display(self):
        print(self.name, self._age)


p = Person('Raj', 30)
print(p.age + 1)
p.age = 40
p.display()

