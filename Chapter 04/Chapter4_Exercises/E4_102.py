x = 3
y = 2
temp = x  # save old value of x
x = y * x    # change x
y = temp   # set y to old value of x
print(x, y)

x = 3
y = 2
x, y = y*x, x
print(x, y)