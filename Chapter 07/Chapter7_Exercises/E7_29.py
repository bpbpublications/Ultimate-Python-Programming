text = 'To expect, or to accept, that is the question'
count = dict.fromkeys('aeiou', 0)
for ch in text.lower():
    if ch.lower() in {'a', 'e', 'i', 'o', 'u'}:
        count[ch] += 1
print(count)
