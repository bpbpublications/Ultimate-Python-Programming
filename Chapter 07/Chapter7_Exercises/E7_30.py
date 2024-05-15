number1 = int(input('Enter first number : '))
number2 = int(input('Enter second number : '))

n1 = number1
n2 = number2

p = 0
while n1 >= 1:
    if n1 % 2 != 0:  # if n1 is odd
        p += n2
    n1 //= 2
    n2 *= 2

print(f'{number1} multiplied with {number2} is {p}')
