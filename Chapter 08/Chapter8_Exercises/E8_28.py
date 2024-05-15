message = 'Hello World'
emessage = ''
for i, ch in enumerate(message):
    if i % 2 == 0:
        emessage += chr(ord(ch) + 1)
    else:
        emessage += chr(ord(ch) - 1)
print(emessage)

# Decrypt
dmessage = ''
for i, ch in enumerate(emessage):
    if i % 2 == 0:
        dmessage += chr(ord(ch) - 1)
    else:
        dmessage += chr(ord(ch) + 1)
print(dmessage)
