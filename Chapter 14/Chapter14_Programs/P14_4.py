class Person:
    def set_details(self):
        self.name = 'John'
        self.age = 20

    def display(self):
        print('I am a person', self)

    def greet(self):
        print('Hi, how are you doing ? ', self)


p1 = Person()
p1.set_details()
p2 = Person()
p2.set_details()
print(p1.name, p1.age)
print(p2.name, p2.age)
