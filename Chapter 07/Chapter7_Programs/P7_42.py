for n in range(2, 100):
    is_prime = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=' ')

print()

for n in range(2, 100):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            break
    else:
        print(n, end=' ')
