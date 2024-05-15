
with open('students_info.txt', 'r') as f1, open('sorted_students.txt', 'w') as f2:
    for line in sorted(f1.readlines()):
        f2.write(line)

