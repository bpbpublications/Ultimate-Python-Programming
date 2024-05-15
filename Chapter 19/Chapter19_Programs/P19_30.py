students = [{'name': 'John',
             'city': 'Paris',
             'marks': 21,
             },
            {'name': 'Dev',
             'city': 'London',
             'marks': 23,
             },
            {'name': 'Mary',
             'city': 'Paris',
             'marks': 22,
             }
            ]
print(max(student['marks'] for student in students))
print(max(students, key=lambda d: d['marks']))

topper = max(students, key=lambda d: d['marks'])
print(topper['name'])

print(max(students, key=lambda d: d['marks'])['name'])

print(any(student['city'] == 'Paris' for student in students))
