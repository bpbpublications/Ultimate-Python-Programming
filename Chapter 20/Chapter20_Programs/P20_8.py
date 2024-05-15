try:
    x = int(input('Enter a number : '))
    print(10 / x)
except ValueError:
    print('ValueError exception handled')
    print(3 + 'x')
finally:
    print('Running clean up code')
print('End ……')
