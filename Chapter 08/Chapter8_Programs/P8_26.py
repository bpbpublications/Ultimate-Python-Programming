while True:
    print('1. Add two numbers')
    print('2. Subtract first number from second number')
    print('3. Subtract second number from first number')
    print('4. Multiply two numbers')
    print('5. Exit')

    choice = int(input('Enter your choice : '))

    if choice == 5:
        break
    if choice < 1 or choice > 4:
        print('Wrong choice')
        continue

    x = int(input('Enter first number : '))
    y = int(input('Enter second number : '))

    if choice == 1:
        print(x + y)
    elif choice == 2:
        print(y - x)
    elif choice == 3:
        print(x - y)
    elif choice == 4:
        print(x * y)
