with open('zenpython.txt', 'r') as f:
    while True:
        s = f.readline()
        if s == '':
            break
        print(s, end='')
