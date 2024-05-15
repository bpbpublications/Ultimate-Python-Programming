with open('students_info.txt', 'r') as f1, open('invitation.txt', 'r') as f2:
    message = f2.read()
    for line in f1:
        name, gender, *_ = line.split(':')
        name, gender = name.strip(), gender.strip()
        greeting = 'Dear ' + ('Mr ' if gender == 'Male' else 'Ms ') + name + ',\n'
        with open(name + 'Invitation.txt', 'w') as f:
            f.write(greeting + message)
