def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def primes(x, y):
    return [n for n in range(x, y + 1) if is_prime(n)]


def twin_primes(x, y):
    tp = []
    for i in range(x, y + 1):
        if is_prime(i) and is_prime(i + 2):
            tp.append((i, i + 2))
    return tp

if __name__ == '__main__':
    print(is_prime(4))
    print(is_prime(5))
    print(primes(20, 40))
    print(twin_primes(3, 61))
