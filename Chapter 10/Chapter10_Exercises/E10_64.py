def subtract(a, b):
    print(a - b)


def add(a, b):
    print(a + b)


def multiply(a, b):
    print(a * b)


def divide(a, b):
    print(a // b)


d = {'a': add, 's': subtract, 'm': multiply, 'd': divide}
choice = ''
while choice != 'q':
    print('a - Add')
    print('s - Subtract')
    print('m - Multiply')
    print('d - Divide')
    print('q - Quit\n')

    choice = input('Enter your choice :')
    if choice == 'q':
        break
    x = int(input('Enter a number : '))
    y = int(input('Enter another number : '))

    d[choice](x, y)
