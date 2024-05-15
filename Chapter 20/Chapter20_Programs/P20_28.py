try:
    age = int(input('Enter age : '))
    if age < 0 or age > 120:
        raise ValueError
except ValueError:
    print('Invalid value for age')
else:
    print('Age is', age)
