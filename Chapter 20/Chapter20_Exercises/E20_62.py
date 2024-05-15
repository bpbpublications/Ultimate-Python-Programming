def factorial(n):
    if not isinstance(n, int):
        raise TypeError('argument to factorial should be an integer')
    if n < 0:
        raise ValueError('argument to factorial should not be negative')
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact


print(factorial(5))
#print(factorial(-5))
#print(factorial('five'))
