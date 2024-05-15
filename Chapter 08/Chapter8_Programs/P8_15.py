students = ['Era', 'Ted', 'Rob', 'Joe', 'Amy', 'Sam', 'Pat', 'Joy', 'Tia']
failed_students = ['Ted', 'Amy', 'Sam']

for student in students:
    if student in failed_students:
        students.remove(student)
print(students)

students = ['Era', 'Ted', 'Rob', 'Joe', 'Amy', 'Sam', 'Pat', 'Joy', 'Tia']
failed_students = ['Ted', 'Amy', 'Sam']

for student in students[:]:
    if student in failed_students:
        students.remove(student)
print(students)
