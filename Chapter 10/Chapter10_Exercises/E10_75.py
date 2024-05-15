def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def twin_primes(x, y):
    tp = []
    for i in range(x, y + 1):
        if is_prime(i) and is_prime(i + 2):
            tp.append((i, i + 2))
    return tp


print(twin_primes(10, 70))
