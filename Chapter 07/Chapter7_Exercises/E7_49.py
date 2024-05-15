n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end='')
    print()

n = 4
for i in range(1, n + 1):
    x = 10
    for j in range(1, i + 1):
        print(x, end=' ')
        x += 1
    print()

n = 4
x = 10
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(x, end=' ')
        x += 1
    print()

n = 4
for i in range(1, n + 1):
    x = 'A'
    for j in range(1, i + 1):
        print(x, end='')
        x = chr(ord(x) + 1)
    print()

n = 4
x = 'A'
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(x, end='')
    x = chr(ord(x) + 1)
    print()

n = 4
x = 'A'
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(x, end='')
        x = chr(ord(x) + 1)
    print()
