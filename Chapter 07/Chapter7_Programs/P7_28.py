import pprint

students = {105416: {'name': 'John',
                     'gender': 'M',
                     'city': 'Paris',
                     'age': 21,
                     'marks': {'Maths': 89, 'Physics': 78, 'Chemistry': 91},
                     'is_sporty': True},

            144547: {'name': 'Dev',
                     'gender': 'M',
                     'city': 'London',
                     'age': 23,
                     'marks': {'Maths': 88, 'Physics': 77, 'Chemistry': 98},
                     'is_sporty': False},

            132399: {'name': 'Mary',
                     'gender': 'F',
                     'city': 'Paris',
                     'age': 22,
                     'marks': {'Maths': 99, 'Physics': 87, 'Chemistry': 88},
                     'is_sporty': True}
            }

for student in students.values():
    total = 0
    for marks in student['marks'].values():
        total += marks
    student['total'] = total

pprint.pp(students)

print(f"{'id':8}{'Name':8}{'Age':>5}{'Maths':>10}{'Physics':>10}{'Chemistry':>10}{'Total':>7}")
for id_num, student in students.items():
    print(f'{id_num: <8}', end='')
    print(f'{student["name"]:8}', end='')
    print(f'{student["age"]:5}', end='')
    for marks in student["marks"].values():
        print(f'{marks:10}', end='')
    print(f'{student["total"]:7}')
