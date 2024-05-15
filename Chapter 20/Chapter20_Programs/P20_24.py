try:
    try:
        x = int(input('Enter a number : '))
        print(10 / x)
    except ValueError as e:
        print('ValueError exception occurred : ', e)
except ZeroDivisionError:
    print('Cannot divide by zero')
