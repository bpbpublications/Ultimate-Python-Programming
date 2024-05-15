n = 5
i = 1
s = 0
while i <= n:
    s += i
    i += 1
print(s)

n = 5
s = 0
for i in range(1, n + 1):
    s += i
print(s)

n = 5
print(sum(range(1, n + 1)))
