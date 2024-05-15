message = 'Hello World !'
emessage = ''
for ch in message:
     emessage += chr(ord(ch) + 1)
print(emessage)


dmessage = ''
for ch in emessage:
        dmessage += chr(ord(ch) - 1)
print(dmessage)
