students = {'12AB': {'name': 'Joe', 'age': 13, 'grade': 'A'},
            '17CD': {'name': 'Sam', 'age': 14, 'grade': 'A+'},
            '42CR': {'name': 'Ted', 'age': 13, 'grade': 'A+'},
            '13CR': {'name': 'Bob', 'age': 13, 'grade': 'B+'},
            '19FD': {'name': 'Rob', 'age': 12, 'grade': 'A+'}}

L1 = [record['name'] for record in students.values() if record['grade'] == 'A+']
print(L1)

L2 = [(id, record['name']) for id, record in students.items() if record['grade'] == 'A+']
print(L2)

