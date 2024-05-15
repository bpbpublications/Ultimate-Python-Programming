text = 'Hello !!! My name is Anthony Gonsalves, and you are .... ??'
s = {ch for ch in text if not ch.isalnum()}
print(s)
L  = [ch for ch in text if not ch.isalnum()]
print(L)
s1 = {ch for ch in text.lower() if ch.isalpha() and ch not in 'aeiou'}
print(s1)





