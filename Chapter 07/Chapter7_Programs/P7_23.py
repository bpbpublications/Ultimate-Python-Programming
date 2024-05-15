D = {'apple': 50, 'banana': 25, 'guava': 40, 'grapes': 34, 'orange': 30}
for fruit in D:
    print(f'{fruit:8}', end='  ')
    for i in range(D[fruit]):
        print('=', end='')
    print()

for fruit in D:
    print(f'{fruit:8}', end='  ')
    print('=' * D[fruit], end='')
    print()
