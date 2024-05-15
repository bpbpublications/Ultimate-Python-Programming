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

    @age.deleter
    def age(self):
        del self._age
        print('age deleted')

    def display(self):
        print(self.name, self._age)


p = Person('Jill', 25)
print(p.age)
del p.age
