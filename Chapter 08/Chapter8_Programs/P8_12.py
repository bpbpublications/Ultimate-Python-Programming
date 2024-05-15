numbers = [23, 78, 98, 78, 65, -36, 78, 99]
for number in numbers:
    if number < 0:
        print(f'Found negative number {number}')
        break
else:
    print('No negative number in the list')

numbers = [23, 78, 98, 78, 65, -36, 78, 99]
for i, number in enumerate(numbers):
    if number < 0:
        print(f'Found negative number {number} at index {i}')
        break
else:
    print('No negative number in the list')
