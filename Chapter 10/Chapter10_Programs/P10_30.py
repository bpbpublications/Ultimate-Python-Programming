def sum_of_squares(L):
    s = 0
    for n in L:
        s += n * n
    return s


numbers = [1, 2, 3, 5, 6]
s = sum_of_squares(numbers)
print('Sum of squares =', s)
print(numbers)

