primes = []
for n in range(100, 300):
    for i in range(2, n // 2):
        if n % i == 0:
            break
    else:
        primes.append(n)
print(primes)
