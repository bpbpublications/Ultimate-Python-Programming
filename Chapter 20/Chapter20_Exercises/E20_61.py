minimum = 18
maximum = 60

try:
    age = int(input('Enter age : '))
    if age < minimum or age > maximum:
        raise ValueError(minimum, maximum)
except ValueError as e:
    print('Invalid age value')
    if len(e.args) == 2:
        print('Value of age should be in between', e.args[0], 'and', e.args[1])
else:
    print(age)
