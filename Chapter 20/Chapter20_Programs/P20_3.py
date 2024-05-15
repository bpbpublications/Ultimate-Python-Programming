boys = int(input('Enter number of boys '))
girls = int(input('Enter number of girls '))

if girls == 0:
    print('No girls, Ratio not defined')
else:
    print('Ratio of boys to girls is', boys / girls)

try:
    print('Ratio of boys to girls is ', boys / girls)
except ZeroDivisionError:
    print('No girls, Ratio not defined')

