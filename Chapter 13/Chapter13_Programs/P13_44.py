with open('students_info.txt', 'r') as f1, \
        open('highperformers.txt', 'w') as f2, \
        open('potentialperformers.txt', 'w') as f3, \
        open('lowperformers.txt', 'w') as f4:
    for line in f1:
        rollno, name, *pairs, _ = line.split(':')
        total = 0
        for pair in pairs:
            _, marks = pair.split('-')
            marks = int(marks.strip())
            total += marks
        percentage = total / len(pairs)
        if percentage >= 80:
            print(f'{rollno} {name:12} {percentage:8.2f}%', file=f2)
        elif percentage >= 50:
            print(f'{rollno} {name:12} {percentage:8.2f}%', file=f3)
        else:
            print(f'{rollno} {name:12} {percentage:8.2f}%', file=f4)
