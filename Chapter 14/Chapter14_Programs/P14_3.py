class Person:
    def display(self):
        print('I am a person', self)

    def greet(self):
        print('Hi, how are you doing ? ', self)


p1 = Person()
p2 = Person()
p1.display()
p1.greet()
p2.display()
p2.greet()
