numbers = [11, 20, 30, 24, 67, 30, 14, 30, 67, 52, 20]
d = {}
for number in numbers:
    d[number] = [i for i, item in enumerate(numbers) if item == number]
print(d)