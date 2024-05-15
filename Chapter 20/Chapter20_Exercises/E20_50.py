try:
    age = int(input('Enter age  : '))
except ValueError:
    print('Not a valid integer value')
else:
    if age < 0 or age > 120:
        print('Age cannot be more than 120 or less than 0')
    else:
        print('Age is', age)

