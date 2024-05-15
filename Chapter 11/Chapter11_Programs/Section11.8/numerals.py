def is_even(num):
    return num % 2 == 0

def reverse(num):
    return int(str(num)[::-1])

def sum_digits(num):
    s = 0
    while num != 0:
        s += num % 10
        num //= 10
    return s

def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact

def _func():
   pass

