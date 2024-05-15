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


print(type(greet), id(greet), greet)
print(type(greet1), id(greet1), greet1)
print(type(calculate), id(calculate), calculate)
print(type(print_blank_lines), id(print_blank_lines), print_blank_lines)
