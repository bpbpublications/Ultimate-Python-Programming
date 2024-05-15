x = int(input('Enter a number : '))
y = int(input('Enter another number : '))

print('1. Add the two numbers')
print('2. Subtract first from second')
print('3. Subtract second from first')
print('4. Multiply the two numbers')
print('5. Divide first by second')
print('6. Divide second by first')

choice = input('Enter your choice : ')

if choice == '1':
    print(x + y)
elif choice == '2':
    print(y - x)
elif choice == '3':
    print(x - y)
elif choice == '4':
    print(x * y)
elif choice == '5':
    print(x / y)
elif choice == '6':
    print(y / x)
else:
    print('Wrong choice')
