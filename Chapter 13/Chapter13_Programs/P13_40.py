with open('employees_info.txt', 'r') as f:
    for line in f:
        _, name, _, phone, salary = line.split(':')
        salary = float(salary.strip())
        bonus = 0.5 * salary if salary < 20000 else 0.3 * salary
        print(name, phone, bonus)
