class Person:
    def set_details(name, age):
        self.name = name
        self.age = age

    def display(self):
        print('I am', self.name)

    def greet(self):
        if self.age < 80:
            print('Hi, how are you doing?')
        else:
            print('Hello, how do you do?')
        self.display()


p1 = Person()
p1.set_details('Bob', 20)
p1.greet()

p2 = Person()
p2.set_details('Ted', 90)
p2.greet()
