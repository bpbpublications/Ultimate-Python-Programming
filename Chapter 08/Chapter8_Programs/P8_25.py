x = int(input('Enter a number : '))
y = int(input('Enter another number : '))
print('1. Add the two numbers')
print('2. Subtract first from second')
print('3. Subtract second from first')
print('4. Multiply the two numbers')

choice = int(input('Enter your choice : '))

if choice == 1:
    print(x + y)
elif choice == 2:
    print(y - x)
elif choice == 3:
    print(x - y)
elif choice == 4:
    print(x * y)
else:
    print('Wrong choice')

