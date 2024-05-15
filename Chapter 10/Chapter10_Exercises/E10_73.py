def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return n


def func(x):
    for i in range(1, x + 1):
        print(fizzbuzz(i))


func(50)
