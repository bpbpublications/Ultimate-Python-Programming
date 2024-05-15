from student import Student

s = Student('Raj', 987654535, [73, 89, 78, 88])

s.display()
if s._calculate_total() > 160:
    print('Pass')
else:
    print('Fail')
