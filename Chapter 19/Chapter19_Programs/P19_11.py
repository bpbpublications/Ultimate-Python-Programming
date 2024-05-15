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

L = [s1, s2, s3]
# L.sort()  # Will give TypeError: '<' not supported between instances of 'Student' and 'Student'

L.sort(key=lambda s: s.marks)
for i in L:
    print(i)
