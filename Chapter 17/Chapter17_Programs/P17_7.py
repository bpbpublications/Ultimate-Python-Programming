L = [1, 2, 3]
for item in L:
    print(item)

L = [1, 2, 3]
it = iter(L)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
