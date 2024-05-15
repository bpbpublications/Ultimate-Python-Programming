class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

    def greet(self):
        if self.age < 80:
            print('Hi, how are you doing?')
        else:
            print('Hello, how do you do?')

    def __lt__(self, other):
        return self.age < other.age


p1 = Person('Tom', 20)
p2 = Person('Bob', 15)
p3 = Person('Yug', 32)
p4 = Person('Sam', 80)
p5 = Person('Jim', 19)
p6 = Person('Kim', 32)

guests = [p1, p2, p3, p4, p5, p6]

for guest in sorted(guests):
    print(guest)

youngest = min(guests)
oldest = max(guests)

print('Youngest guest is', youngest)
print('Oldest guest is', oldest)
