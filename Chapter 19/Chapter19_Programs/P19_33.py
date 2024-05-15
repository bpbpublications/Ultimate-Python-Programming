from operator import attrgetter


class Student:
    def __init__(self, name, marks, birthYear):
        self.name = name
        self.marks = marks
        self.birthYear = birthYear

    def __str__(self):
        return f'{self.name} {self.marks} {self.birthYear}'


s1 = Student('John', 97, 1988)
s2 = Student('Sam', 89, 1987)
s3 = Student('Pam', 99, 1982)
s4 = Student('Pam', 99, 1978)

L = [s1, s2, s3, s4]

L.sort(key=attrgetter('marks'))
for i in L:
    print(i)

print()

L.sort(key=attrgetter('marks', 'birthYear'))

for i in L:
    print(i)
