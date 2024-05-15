text = 'Hello world !!!   '
count = {}
for character in text:
    count[character] = count.get(character, 0) + 1
print(count)
