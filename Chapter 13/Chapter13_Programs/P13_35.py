def append(file1, *args):
    with open(file1, 'a') as f1:
        for file in args:
            with open(file, 'r') as f2:
                for line in f2:
                    f1.write(line)


append('school.txt', 'class1.txt', 'class2.txt', 'class3.txt')
append('people.txt', 'students.txt', 'employees.txt')
