from operator import itemgetter

employees = [('Rajendra', 'Kumar', 32, 6000),
             ('Sam', 'Saxena', 43, 8000),
             ('Shyamchandra', 'Verma', 23, 3000),
             ('Sam', 'Gupta', 33, 7000),
             ('Sam', 'Sung', 31, 5000)
             ]

print(sorted(employees, key=lambda t: t[2]))

print(sorted(employees, key=itemgetter(2)))

print(sorted(employees, key=itemgetter(1, 2)))
