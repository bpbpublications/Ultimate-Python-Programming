L = ['abc12*', 'xyz45!', '12pqr%', '(lmn)']
for string in L:
    for ch in string:
        if ch.isalpha():
            print(ch, end='')
    print()
