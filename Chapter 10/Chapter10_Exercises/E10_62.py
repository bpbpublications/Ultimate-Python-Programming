def display1(n):
    if n == 0:
        return
    print(n, end=' ')
    display1(n - 1)


def display2(n):
    if n == 0:
        return
    display2(n - 1)
    print(n, end=' ')


display1(5)
print()
display2(5)
