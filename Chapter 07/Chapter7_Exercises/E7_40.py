students = {105416: {'name': 'John',
                     'age': 21,
                     'marks': {'Maths': 89,
                               'Physics': 78,
                               'Chemistry': 91}
                     },
            144547: {'name': 'Dev',
                     'age': 23,
                     'marks': {'Maths': 88,
                               'Physics': 77,
                               'Chemistry': 98}
                     },
            132399: {'name': 'Mary',
                     'age': 22,
                     'marks': {'Maths': 99,
                               'Physics': 87,
                               'Chemistry': 88},
                     }
            }

done_entering = False

while not done_entering:
    id_num = input('Enter id number : ')
    students[id_num] = {}
    students[id_num]['name'] = input('Enter name : ')
    students[id_num]['age'] = int(input('Enter age : '))
    students[id_num]['marks'] = {}
    students[id_num]['marks']['maths'] = int(input('Enter marks in maths : '))
    students[id_num]['marks']['physics'] = int(input('Enter marks in physics : '))
    students[id_num]['marks']['chemistry'] = int(input('Enter marks in chemistry : '))

    done_entering = input('Press Enter to keep entering, anything else to stop')

for id, student in students.items():
    print(id)
    for key, value in student.items():
        print(key, '->', value)
    print('-' * 40)
