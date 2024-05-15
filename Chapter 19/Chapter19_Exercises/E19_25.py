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

L1 = sorted(L, key=lambda x: x.name)
for t in L1:
    print(t, end=' ')
print()
L2 = sorted(L, key=lambda x: x.salary)
for t in L2:
    print(t, end=' ')
