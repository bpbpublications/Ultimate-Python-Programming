def display(L, *, negative=True, odd=True):
    for n in L:
        if n < 0 and negative is False:
            continue
        if n % 2 != 0 and odd is False:
            continue
        print(n, end=' ')
    print()


numbers = [12, -1, 3, 6, 8, 9, 38, -3, 34, -4]

# display(numbers, True, False)
# display(numbers, False)
display(numbers, odd=False)
display(numbers, negative=False)
display(numbers, negative=False, odd=False)
