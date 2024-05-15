n = int(input('Enter a number : '))

is_prime = True
for i in range(2, n // 2 + 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime == True:
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')

for n in range(2, 100):
    isprime = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            isprime = False
            break
    if isprime:
        print(n, end=' ')
