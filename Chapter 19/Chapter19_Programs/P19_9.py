employees = [('Rajendra', 'Kumar', 32, 6000),
             ('Sam', 'Saxena', 43, 8000),
             ('Shyamchandra', 'Verma', 23, 3000),
             ('Sam', 'Gupta', 33, 7000),
             ('Sam', 'Sung', 31, 5000)
             ]

print(max(employees, key = lambda x: x[3]))
print(min(employees, key = lambda x: x[2]))
