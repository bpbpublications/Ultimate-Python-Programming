# Using if..eif..else
value = int(input('Enter value : '))
if value == 0:
    print('Sunday')
elif value == 1:
    print('Monday')
elif value == 2:
    print('Tuesday')
elif value == 3:
    print('Wednesday')
elif value == 4:
    print('Thursday')
elif value == 5:
    print('Friday')
elif value == 6:
    print('Saturday')
else:
    print('Invalid')

# Using dictionary
value = int(input('Enter value : '))
d = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
print(d.get(value, 'Invalid'))

# Python 3,10 onwards, match case can be used to write this code
value = int(input('Enter value : '))
match value:
    case 0:
        print('Sunday')
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case _:
        print('Invalid')
