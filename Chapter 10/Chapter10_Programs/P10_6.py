def display_list(L, base):
    if base == 2:
        ch = 'b'
    elif base == 8:
        ch = 'o'
    elif base == 16:
        ch = 'X'
    else:
        ch = 'd'

    for n in L:
        print(f"{n:{ch}}", end=' ')
    print()

numbers = [134, 2567, 366, 521, 689]

display_list(numbers, 10)
display_list(numbers, 2)
display_list(numbers, 8)
display_list(numbers, 16)
