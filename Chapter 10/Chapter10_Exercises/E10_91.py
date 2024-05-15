def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def sum_digits(n):
    if n // 10 == 0:
        return n
    return n % 10 + sum_digits(n // 10)


print(fact(4), sum_digits(2345))


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def sum_digits(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


print(fact(4), sum_digits(2345))
