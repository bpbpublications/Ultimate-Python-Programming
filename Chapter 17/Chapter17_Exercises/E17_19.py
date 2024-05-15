def gfn():
    x = 1
    while True:
        if x <= 5:
            yield x
        else:
            return
        x += 1


for n in gfn():
    print(n, end=' ')
