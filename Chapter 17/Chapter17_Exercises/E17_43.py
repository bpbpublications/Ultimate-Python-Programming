def primes():
    n = 2
    while True:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                break
        else:
            yield n
        n += 1

x = primes()

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

p = primes()
total = 0
for i in range(5):
    total += next(p)
print(total)
