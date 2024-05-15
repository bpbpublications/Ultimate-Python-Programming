def average(*args):
    print(args)
    return sum(args) / len(args)


x = {98, 23, 85, 56, 12}
y = (48, 98)
z = [67, 89, 43, 78]

print(average(*x, *y, *z))
