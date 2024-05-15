courses_data = {'Python': {'Average': ['Tom', 'Jim'], 'Bright': ['John', 'Tim', 'Ria']},
                'SQL': {'Average': ['Ken', 'Ben', 'Ron'], 'Bright': ['Max', 'Nia']},
                'Web Design': {'Average': ['Geo', 'Ray', 'Leo'], 'Bright': ['Sam'], 'Excellent':
                    ['Roe', 'Pam']},
                }

target = input('Enter name : ')
found = False
for course, data in courses_data.items():
    for category, names_list in data.items():
        for rank, name in enumerate(names_list, 1):
            if target == name:
                found = True
                break
        if found:
            break
    if found:
        break

if found:
    print('Name : ', name)
    print('Course :', course)
    print('Category : ', category)
    print('Rank : ', rank)
else:
    print(target, 'not found')


class FoundException(Exception):
    pass


courses_data = {'Python': {'Average': ['Tom', 'Jim'], 'Bright': ['John', 'Tim', 'Ria']},
                'SQL': {'Average': ['Ken', 'Ben', 'Ron'], 'Bright': ['Max', 'Nia']},
                'Web Design': {'Average': ['Geo', 'Ray', 'Leo'], 'Bright': ['Sam'], 'Excellent': ['Roe', 'Pam']}
                }

target = input('Enter name : ')
try:
    for course, data in courses_data.items():
        for category, names_list in data.items():
            for rank, name in enumerate(names_list, 1):
                if target == name:
                    raise FoundException()
except FoundException:
    print('Name : ', name)
    print('Course :', course)
    print('Category : ', category)
    print('Rank : ', rank)
else:
    print(target, 'not found')
