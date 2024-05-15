boys = int(input('Enter number of boys '))
girls = int(input('Enter number of girls '))

try:
    r = boys / girls
    print(f'Ratio of boys to girls is {r}')
except ZeroDivisionError:
    print('No girls, Ratio not defined')

total = boys + girls
print(f'Total number of students = {total}')
