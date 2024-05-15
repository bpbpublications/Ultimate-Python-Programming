n = 10
x, y = 0, 1
for i in range(n):
    print(x, end=' ')
    x, y = y, x + y
print()

n = 200
x, y = 0, 1
while x < n:
    print(x, end=' ')
    x, y = y, x + y
print()



