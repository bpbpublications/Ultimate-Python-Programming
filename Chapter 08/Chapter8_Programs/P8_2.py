primes = {31, 3, 5, 11, 2, 13, 17, 43, 19, 7, 37, 23, 29, 41}

for number in primes:
    print(number, end=' ')

print()

for number in sorted(primes):
    print(number, end=' ')

print()

for number in reversed(sorted(primes)):
    print(number, end=' ')

print()

for number in sorted(primes, reverse=True):
    print(number, end=' ')
