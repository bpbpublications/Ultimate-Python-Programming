marks = int(input('Enter marks - '))

if marks >= 70:
    grade = 'A'
if marks >= 60 and marks < 70:
    grade = 'B'
if marks >= 50 and marks < 60:
    grade = 'C'
if marks >= 40 and marks < 50:
    grade = 'D'
if marks < 40:
    grade = 'E'
print(f'Student gets {grade} grade')
