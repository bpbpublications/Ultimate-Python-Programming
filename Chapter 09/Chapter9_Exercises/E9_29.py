students = {105416: {'name': 'John',
                     'city': 'Paris',
                     'dob': '12-01-2000',
                     'marks': {'Maths': 89,
                               'Physics': 78,
                               'Chemistry': 91},
                     },

            144547: {'name': 'Dev',
                     'city': 'London',
                     'dob': '13-11-1998',
                     'marks': {'Maths': 58,
                               'Physics': 57,
                               'Chemistry': 68},
                     },

            132399: {'name': 'Mary',
                     'city': 'Paris',
                     'dob': '01-05-1997',
                     'marks': {'Maths': 99,
                               'Physics': 87,
                               'Chemistry': 88},
                     }
            }

L = [student['name'] for student in students.values() if sum(student['marks'].values()) > 200]
print(L)

