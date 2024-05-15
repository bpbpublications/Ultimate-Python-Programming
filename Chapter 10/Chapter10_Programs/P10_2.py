def greet():
    print('Hello')


def greet1(name):
    print('Hello', name)


def calculate(a, b):
    print(a + b)
    print(a - b)
    print(a * b)


def print_blank_lines(n):
    for i in range(n):
        print()


greet()
greet()
greet()

greet1('Sam')
greet1('Bob')

calculate(8, 5)
calculate(6.5, 4)

