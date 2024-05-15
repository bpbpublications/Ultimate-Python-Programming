numbers = [23, 78, 98, 78, 65, -36, 78, 99]
found = False
for number in numbers:
    if number < 0:
        print('Found a negative number')
        found = True
        break
if not found:
    print('No negative number in the list')


for number in numbers:
    if number < 0:
        print('Found a negative number')
        break
else:
    print('No negative number in the list')
