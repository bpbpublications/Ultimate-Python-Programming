message = 'Hello World'
for ch in message:
    print(ch, end=' ')

print()

for ch in message:
    if ch in {'a', 'e', 'i', 'o', 'u'}:
        print(ch, end=' ')
