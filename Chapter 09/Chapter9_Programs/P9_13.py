
students = ['Era', 'Ted', 'Rob', 'Joe', 'Amy', 'Sam', 'Pat', 'Joy', 'Tia']
failed_students = ['Ted', 'Amy', 'Sam']
students = [stu for stu in students if stu not in failed_students]
print(students)



