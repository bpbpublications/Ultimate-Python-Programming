data = [2, 1, 3, 4, 5, 6, 9, 1, 7, 8, 9]
for i in range(4):
    print(data[i], end=' ')

print()

for i in range(0, len(data), 3):
    print(data[i], end=' ')

print()

for item in data[:4]:
    print(item, end=' ')

print()

for item in data[::3]:
    print(item, end=' ')
