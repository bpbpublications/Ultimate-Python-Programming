def func(s):
    vowels = 0
    consonants = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


text = 'Hello world'
v, c = func(text)
print("Number of vowels = ", v)
print("Number of consonants = ", c)

