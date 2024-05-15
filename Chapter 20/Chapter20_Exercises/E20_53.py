
import math

while True:
    try:
        n = int(input('Enter a number : '))
        f = math.factorial(n)
    except ValueError as e:
        print(e)
    else:
        print('Factorial of the number is ', f)
        break
