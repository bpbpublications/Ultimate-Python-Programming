def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


x = 10
y = 4

if is_divisible(x, 3):
    print('Do something.')

if not is_divisible(x, y):
    print('Do something..')

if is_prime(x):
    print('Do something...')

if not is_prime(x):
    print('Do something....')
