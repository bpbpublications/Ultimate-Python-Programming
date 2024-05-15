minimum = 18
maximum = 60

try:
    age = int(input('Enter age : '))
    if age < minimum or age > maximum:
        raise ValueError(f'Age not in valid range {minimum}-{maximum} ')
except ValueError as e:
    print('Invalid age value')
    print(e)
else:
    print(age)
