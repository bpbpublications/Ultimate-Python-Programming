mylist = [1, 2, 'n', 3, 'one', 4]


def sum1(L):
    if not L:
        return 0
    elif not isinstance(L[0], int):
        return sum1(L[1:])
    else:
        return L[0] + sum1(L[1:])


print(sum1(mylist))
