L = ['this', 'that', 'here', 'there']
# Encrypt
for i, word in enumerate(L):
    new_word = ''
    for ch in word:
        new_word += chr(ord(ch) + 1)
    L[i] = new_word
print(L)

# Decrypt
for i, word in enumerate(L):
    new_word = ''
    for ch in word:
        new_word += chr(ord(ch) - 1)
    L[i] = new_word
print(L)
