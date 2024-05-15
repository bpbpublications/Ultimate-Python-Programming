first = int(input('Enter a number : '))
second = int(input('Enter another number : '))

print(f'{first = }, {second = }')

if first < second:
    print(f'{first * second = }')
else:
    print(f'{first / second = }')

x = 40 / first + second

print(f'{x = }')
