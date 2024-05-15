def sum2(L):
    total = 0
    for item in L:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += sum2(item)
        else:
            pass

    return total


L = [[2, 3], [1, 4, 'k', 3], [2], 'x', [5, 6, 2, 1]]
print(sum2(L))
