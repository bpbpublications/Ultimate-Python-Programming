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
print(students[144547])
print(students[105416]['name'])
print(students[132399]['marks']['Chemistry'])

