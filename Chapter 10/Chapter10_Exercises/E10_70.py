def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

print(factorial(4))
