def func(x, y, z):
    x = 100 - x
    y *= 2
    z += 5
    return x, y, z

n1 = 2
n2 = 3
n3 = 4

n1, n2, n3 = func(n1, n2, n3)
print(n1, n2, n3)
