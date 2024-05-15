data = [2, 3, 1, 4, 7, 5]
max_even = 0
for item in data:
    if item % 2 == 0 and item > max_even:
        max_even = item
if max_even != 0:
    print(f'Largest even number is {max_even}')
else:
    print(f'No even number in the list')

data = [2, 3, 1, 4, 7, 5]
max_even = 0
index = None
for i, item in enumerate(data):
    if item % 2 == 0 and item > max_even:
        max_even = item
        index = i
if max_even != 0:
    print(f'Largest even number is {max_even} at index {index}')
else:
    print(f'No even number in the list')
