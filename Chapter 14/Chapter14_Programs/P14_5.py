class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am a person', self)

    def greet(self):
        print('Hi, how are you doing ? ', self)


p1 = Person()
p1.set_details('Bob', 20)
p2 = Person()
p2.set_details('Ted', 90)
print(p1.name, p1.age)
print(p2.name, p2.age)
