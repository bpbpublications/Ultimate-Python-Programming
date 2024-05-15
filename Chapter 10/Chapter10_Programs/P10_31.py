numbers = [1, 2, 3, 5, 6]

def sum_of_squares(L):
    for i in range(len(L)):
        L[i] *= L[i]
    return sum(L)

s = sum_of_squares(numbers)
print('Sum of squares = ', s)
print(numbers)
