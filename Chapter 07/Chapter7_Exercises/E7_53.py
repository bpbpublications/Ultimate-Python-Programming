L = [1, 2, 4, 5, 6, 8, 9]
target = 2

found = False
for n in L:
    if n == target:
        found = True
        print(f'{target} found')
        break
else:
    print(f'{target} not found')
