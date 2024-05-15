employees = {'Jack': '02-03-1973',
             'John': '09-12-1977',
             'Mark': '09-11-1972',
             'Mary': '08-05-1977',
             }
L1 = [name for name, dob in employees.items() if dob[-4:] == '1977']
print(L1)
