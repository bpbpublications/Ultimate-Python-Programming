number = int(input('Enter a number : '))
n = number
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(f'Factorial of {number} is {fact}')
