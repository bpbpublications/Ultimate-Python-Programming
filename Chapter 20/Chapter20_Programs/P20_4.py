def f1():
    print('function f1 statement 1')
    f2()
    print('function f1 statement 3')

def f2():
    print('function f2 statement 1')
    f3()
    print('function f2 statement 3')

def f3():
    print('function f3 statement 1')
    x = int(input('Enter a number : '))
    print('function f3 statement 3')

print('Program begins')
f1()
print('Program ends')
