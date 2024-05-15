text = input('Enter some text : ')
v = c = d = 0
for ch in text:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            v += 1
        else:
            c += 1
    elif ch.isdigit():
        d += 1
print(f'{v} vowels, {c} consonants, {d} digits')

