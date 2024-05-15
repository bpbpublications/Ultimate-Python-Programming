def summation(n):
    if n == 0:
        return 0
    else:
        return n + summation(n - 1)


print(summation(5))
