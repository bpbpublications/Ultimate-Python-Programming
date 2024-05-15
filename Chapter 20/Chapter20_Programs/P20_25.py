try:
    try:
        x = int(input('Enter a number : '))
        print(10 / x)
    except Exception as e:
        print('An exception occurred : ', e)
except ZeroDivisionError as e:
    print(e)
