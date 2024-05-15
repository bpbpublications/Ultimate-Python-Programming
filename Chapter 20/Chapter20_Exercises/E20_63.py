marks = {'Sam': 20, 'John': 30, 'Tim': 25, 'Jim': 22}

try:
    name = input('Enter name ')
    print(marks[name])
except KeyError as e:
    print(e, 'not present in the dictionary')
