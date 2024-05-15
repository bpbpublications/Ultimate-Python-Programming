def gfn():
    i = 1
    while True:
        yield i
        yield -i
        i += 1


for value in gfn():
    if value == 10:
        break
    print(value, end=' ')
