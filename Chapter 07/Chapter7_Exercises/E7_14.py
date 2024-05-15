for n in range(10, 20):
    isprime = True
    for i in range(2, n):
        if n % i == 0:
            break
            isprime = False
    if isprime:
        print(n, end=' ')
