def display_list_decimal(L):
    for n in L:
        print(n, end=' ')
    print()


def display_list_binary(L):
    for n in L:
        print(f"{n:b}", end=' ')
    print()


def display_list_octal(L):
    for n in L:
        print(f"{n:o}", end=' ')
    print()


def display_list_hexadecimal(L):
    for n in L:
        print(f"{n:X}", end=' ')
    print()


numbers = [134, 2567, 366, 521, 689]

display_list_decimal(numbers)
display_list_binary(numbers)
display_list_octal(numbers)
display_list_hexadecimal(numbers)
