def f1():
    print('AA')
    f2()
    print('BB')


def f2():
    print('CC')
    x = int(input('Enter a number '))
    print(10 % x)
    print('DD')


print('Begin')
f1()
print('End')
