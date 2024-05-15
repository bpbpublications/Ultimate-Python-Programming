numbers = [23, 78, 98, 78, 65, 36, 78, 99, 72, -94, 12]
found = False
for number in numbers:
    if number < 0:
        found = True
        print('Found a negative number in the list')
        break

if not found:
    print('No negative number in the list')
