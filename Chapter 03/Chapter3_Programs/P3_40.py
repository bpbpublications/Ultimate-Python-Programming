name = 'Raj'
age = 23
print('My name is {:8} and I am {:6} years old'.format(name,age))

print('My name is {:^8} and I am {:<6} years old'.format(name, age))

number = 78.386367
print('number is {:10.4}'.format(number))
print('number is {:10.4f}'.format(number))

print('My name is {:*^8} and age is {:.>6}'.format(name, age))
print('My name is {:*^8} and age is {:>06}'.format(name, age))
