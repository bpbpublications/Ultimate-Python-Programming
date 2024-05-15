text = 'this that here this that where this'

substring = 'this'

start_index = 0
found = False
while True:
    index = text.find(substring, start_index)
    if index == -1:
        break
    print(f'{substring} present at index {index}')
    if not found:
        found = True
    start_index = index + 1

if not found:
    print(f'{substring} not found')

