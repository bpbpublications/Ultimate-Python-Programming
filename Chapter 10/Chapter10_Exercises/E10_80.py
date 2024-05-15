def display(L, *, start='', end=''):
    for i in L:
        if i.startswith(start) and i.endswith(end):
            print(i, end=' ')


display(dir(str), start='is', end='r')
