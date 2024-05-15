class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary

    def __str__(self):
        return f'{self.name} {self.subject} {self.salary}'


t1 = Teacher('Ken', 'Physics', 3800)
t2 = Teacher('Sam', 'Maths', 4000)
t3 = Teacher('Tim', 'Maths', 3500)

L = [t1, t2, t3]

L2 = list(map(lambda x: x.name, sorted(L, key=lambda x: x.salary, reverse=True)))
print(L2)