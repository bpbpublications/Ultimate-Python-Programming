phrase = 'colourful umbrella'
for ch in phrase:
    if ch in {'a', 'e', 'i', 'o', 'u'}:
        print(ch, end=' ')
print()

phrase = 'colourful umbrella'
for ch in set(phrase):
    if ch in {'a', 'e', 'i', 'o', 'u'}:
        print(ch, end=' ')
