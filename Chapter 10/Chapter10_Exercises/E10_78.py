def product(*args):
    p = 1
    for n in args:
        p *= n
    return p


print(product(2, 3, 4, 5, 6, 7))
print(product(2, 3, 4))

