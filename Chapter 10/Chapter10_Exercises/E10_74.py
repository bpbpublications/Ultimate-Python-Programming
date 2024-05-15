def func(L):
    evens = odds = 0
    for n in L:
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds


numbers = [2, 13, 19, 4, 23, 5, 1, 78, 98, 12, 17]
e, o = func(numbers)
print(f'{e} even numbers and {o} odd numbers')
