def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


print(compare(23, 4))
print(compare(23, 23))
print(compare(4, 23))
