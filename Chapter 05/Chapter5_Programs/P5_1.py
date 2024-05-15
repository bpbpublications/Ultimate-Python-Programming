student = {'name': 'John',
           'gender': 'M',
           'city': 'Paris',
           'age': 21,
           'marks': [89, 78, 91],
           'is_sporty': True
           }

prices = {'pencil': 10,
          'pen': 22,
          'eraser': 12,
          'sharpener': 13,
          'marker': 32
          }

salary = {'programmer': 10000,
          'manager': 20000,
          'accountant': 15000
          }
print(student['name'], student['city'], student['marks'][1])
total = 2 * prices['pencil'] + 3 * prices['marker'] + 5 * prices['eraser']
print(total)
print(salary['programmer'])
