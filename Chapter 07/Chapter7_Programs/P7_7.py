student_id = int(input('Enter student id (1000-9999) : '))
while student_id < 1000 or student_id > 9999:
    student_id = int(input('Enter student id (1000-9999) : '))
print(student_id)

