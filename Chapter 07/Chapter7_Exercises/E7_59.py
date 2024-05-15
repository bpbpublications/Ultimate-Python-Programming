for n in range(2, 100):
    isprime = True
    for i in range(2, n):
        if n % i == 0:
            print(f'{n} is not prime as {n} = {i} * {n // i}')
            isprime = False
            break
    if isprime:
        print(f'{n} is prime')

