import prime

n1 = 10
n2 = 50
print(f'List of primes from {n1} to {n2}')
print(prime.primes(n1, n2))

print(f'List of twin primes from {n1} to {n2}')
print(prime.twin_primes(n1, n2))
