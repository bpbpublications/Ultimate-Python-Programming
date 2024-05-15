L = [11, 23, 31, 4, 23, 45, 11, 23, 79, 23, 81, 43, 23]
n = 3
item = 23
count = 0
for i, num in enumerate(L):
    if num == item:
        count += 1
    if count == n:
        L.pop(i)
        break
print(L)
