def sum_digits(n):
    if n // 10 == 0:  # n is a single digit number
        return n
    else:
        return n % 10 + sum_digits(n // 10)


print(sum_digits(5432))
