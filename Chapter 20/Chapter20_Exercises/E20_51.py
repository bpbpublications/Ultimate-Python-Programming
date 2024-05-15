while True:
    try:
        age = int(input('Enter age  : '))
    except ValueError:
        print('Please enter a valid integer value')
        continue
    else:
        if age < 0 or age > 120:
            print('Age cannot be more than 120 or less than 0. Please enter again')
        else:
            print('Age is ', age)
            break

while True:
    try:
        age = int(input('Enter age  : '))
    except ValueError:
        print('Please enter a valid integer value')
        continue
    if age < 0 or age > 120:
        print('Age cannot be more than 120 or less than 0. Please enter again')
    else:
        print('Age is ', age)
        break
