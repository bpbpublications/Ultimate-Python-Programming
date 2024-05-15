numbers = [134, 2567, 366, 521, 689]


def display_list(L, base=10):
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


display_list(numbers)
display_list(numbers, 8)
display_list(numbers, 16)
