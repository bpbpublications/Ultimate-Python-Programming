def func(L, n):
    for i in range(len(L)):
        L[i] *= n


numbers = [2, 4, 5, 6, 1]
func(numbers, 3)
print(numbers)
