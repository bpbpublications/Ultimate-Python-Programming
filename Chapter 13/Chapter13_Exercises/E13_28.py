
with open('students_info.txt', 'r') as f:
    with open('boys.txt', 'w') as f1, open('girls.txt', 'w') as f2:
        for line in f:
            _, gender, *_ = line.split(':')
            gender = gender.strip()
            if gender == 'Male':
                f1.write(line)
            else:
                f2.write(line)

