x = range(3, 0, -1)
y = reversed([1, 2, 3])

for i in x:
    for j in x:
        print(f'i={i}, j={j}')

print('----------------------')

for i in y:
    for j in y:
        print(f'i={i}, j={j}')

print(x is iter(x))
print(y is iter(y))

