numbers = [12, -1, 3, 6, 8, 9, 38, -3, 34, -4]


def display(L, negative=True, odd=True):
    for n in L:
        if n < 0 and negative == False:
            continue
        if n % 2 != 0 and odd == False:
            continue
        print(n, end=' ')
    print()


display(numbers)
display(numbers, False)
display(numbers, False, True)
display(numbers, True, False)

display(numbers, odd=False)
display(numbers, negative=False)
display(numbers, negative=False, odd=False)
