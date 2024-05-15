class Person:
    def set_details(self, name, age):
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

    def get_old(self):
        age = 75


p1 = Person()
p1.set_details('Bob', 20)
p1.get_old()
print(p1.age)
