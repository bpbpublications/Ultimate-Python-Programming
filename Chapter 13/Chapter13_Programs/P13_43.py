with open('students_info.txt', 'r') as f1, open('results.txt', 'w') as f2:
    for line in f1:
        rollno, name, *pairs, _ = line.split(':')
        total = 0
        for pair in pairs:
            _, marks = pair.split('-')
            marks = int(marks.strip())
            total += marks
        percentage = total / len(pairs)
        print(f'{rollno} {name:12} {percentage:8.2f}%', file=f2)
