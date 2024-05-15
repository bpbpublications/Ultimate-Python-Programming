L = [2, 9, 3, 4, 1, 2, 5, 7, 8, 3, 6]
prev = None
for item in sorted(L):
    if prev == item:
        print('A duplicate found')
        break
    prev = item
else:
    print('No duplicates')

# Another approach
if len(L) == len(set(L)):
    print('No duplicates')
else:
    print('List has duplicates')

