def square(x):
    return x * x


def add(x, y):
    return x + y


s = square(4)

a = 4
b = 5
c = 3
d = 2

x = square(a) * 10 + b

if 100 < square(x) < 500:
    print('Do something')

if add(a, b) > add(c, d):
    print('Do something')

p = add(square(a), square(b))

r = square(add(a, b))
print(p, r)
print(square(a))
