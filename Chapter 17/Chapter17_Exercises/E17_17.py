def inc_gen():
    i = 1
    while True:
        yield i
        i = i + 1


inc = inc_gen()
print(next(inc), end=' ')
print(next(inc), end=' ')
print(next(inc), end=' ')
