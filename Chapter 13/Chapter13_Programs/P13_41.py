with open('employees_info.txt', 'r') as f, open('employees1.txt', 'w') as f1:
    for line in f:
        empid, name, email, phone, salary = line.rstrip().split(':')
        print(f'{empid:5} : {name:10} : {email:18}: {phone:15}:{salary:>9}', file=f1)
