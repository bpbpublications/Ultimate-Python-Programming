marks = int(input('Enter marks - '))

if marks >= 70:
    grade = 'A'
else:
    if marks >= 60:
        grade = 'B'
    else:
        if marks >= 50:
            grade = 'C'
        else:
            if marks >= 40:
                grade = 'D'
            else:
                grade = 'E'

print(f'Student gets {grade} grade')
