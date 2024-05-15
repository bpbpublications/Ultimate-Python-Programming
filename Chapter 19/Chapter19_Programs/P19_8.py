employees = [('Rajendra', 'Kumar', 32, 6000),
             ('Sam', 'Saxena', 43, 8000),
             ('Shyamchandra', 'Verma', 23, 3000),
             ('Sam', 'Gupta', 33, 7000),
             ('Sam', 'Sung', 31, 5000)
             ]
print(sorted(employees))
print(sorted(employees, key=lambda x: x[2]))
print(sorted(employees, key=lambda x: len(x[0]) + len(x[1])))
print(sorted(employees, key=lambda t: (t[0], t[2])))
print(sorted(employees, key=lambda t: (t[0].upper(), t[2])))
employees.sort(key=lambda x: x[1])
print(employees)
