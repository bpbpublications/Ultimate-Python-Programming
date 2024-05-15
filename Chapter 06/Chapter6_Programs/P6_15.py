marks = int(input('Enter marks - '))

if marks >= 70:
    grade = 'A'
elif marks >= 60:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
elif marks >= 40:
    grade = 'D'
else:
    grade = 'E'

print(f'Student gets {grade} grade')
