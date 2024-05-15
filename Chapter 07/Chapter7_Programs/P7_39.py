student_marks = {'Sam': [46, 37, 38],
                 'Pam': [99, 97, 95],
                 'Ria': [45, 63, 55],
                 'Joe': [34, 36, 34],
                 'Jim': [99, 97, 96],
                 'Ted': [33, 24, 51],
                 'Tim': [78, 98, 79]
                 }

for name, marks in student_marks.items():
    total = sum(marks)

    if total < 120:
        print(f'{name} failed the exam\n')
        continue

    percentage = total / 3

    if percentage < 60:
        grade = 'C'
    elif percentage < 90:
        grade = 'B'
    else:
        grade = 'A'
        if percentage > 95:
            print(f'{name} awarded a scholarship')

    print(f'{name} gets {grade} grade', end=' ')
    print(f'with {percentage:.1f} marks\n')
