marks = int(input('Enter marks - '))

if marks < 40:
    grade = 'E'
elif marks < 50:
    grade = 'D'
elif marks < 60:
    grade = 'C'
elif marks < 70:
    grade = 'B'
else:
    grade = 'A'

print(grade)
