n = int(input('Enter a number : '))
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    n //= 10

print(sum_digits)

