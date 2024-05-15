n = 4
for i in range(1, n + 1):
    print('*' * i)

n = 4
for i in range(1, n + 1):
    print(str(i) * i)

for i in range(ord('A'), ord('F')):
    print(chr(i) * (i - ord('A') + 1))

n = 4
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * i)

n = 4
for i in range(1, n + 1):
    print(' ' * (n - i), end='')  # for printing spaces before asterisks
    print('*' * (2 * i - 1))
