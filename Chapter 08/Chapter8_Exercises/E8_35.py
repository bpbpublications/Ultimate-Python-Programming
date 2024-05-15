D = {'John': [90, 78, 87, 67],
     'Sam': [95, 76, 78, 57],
     'Dev': [80, 69, 59, 45]
     }
subjects = ['Physics', 'Chemistry', 'Maths', 'Biology']
max_marks = [100, 80, 100, 75]
pass_marks = [40, 25, 40, 20]

for name, marks in D.items():
    print(name, end='\n' + '-' * (50) + '\n')
    total = 0
    for subject, mm, pm, score in zip(subjects, max_marks, pass_marks, marks):
        print(f'{subject:10}{mm:4}{pm:4}{score:5}')
        total += score
    per = (total / sum(max_marks)) * 100
    print(f'Total = {total:3}')
    print(f'Percentage = {per:4.2f}')
    print('-' * 50)
