employees = {'Sam': 3000, 'John': 4000, 'Rob': 15000, 'Tina': 9000}
for employee, salary in employees.items():
    if salary > 10000:
        employees.pop(employee)
print(employees)
