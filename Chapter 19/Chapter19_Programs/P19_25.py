class Student:
    def __init__(self, name, marks, birthYear):
        self.name = name
        self.marks = marks
        self.birthYear = birthYear

    def __str__(self):
        return f'{self.name} {self.marks} {self.birthYear}'

    def __repr__(self):
        return f'{self.name} {self.marks} {self.birthYear}'


s1 = Student('John', 97, 1988)
s2 = Student('Sam', 89, 1987)
s3 = Student('Pam', 99, 1985)
s4 = Student('Tim', 91, 1983)
s5 = Student('Jim', 80, 1987)

L = [s1, s2, s3, s4, s5]
new_list = list(filter(lambda x :x.marks > 90, L))
print(new_list)